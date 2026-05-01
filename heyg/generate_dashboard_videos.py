#!/usr/bin/env python3
"""Generate 5 HeyGen videos from Jaci's dashboard task scripts.

Usage:
  python3 generate_dashboard_videos.py <HEYGEN_API_KEY>

Reads dashboard-video-scripts.json, submits all 5 videos to HeyGen API,
polls for completion, downloads results, and deploys to girlgone.ai/heyg/.
"""

import json, os, sys, time, urllib.request, urllib.error, shutil

SCRIPTS_FILE = os.path.join(os.path.dirname(__file__), "dashboard-video-scripts.json")
OUTPUT_DIR = os.path.dirname(__file__)
API_BASE = "https://api.heygen.com"

def api_request(method, path, api_key, data=None):
    url = f"{API_BASE}{path}"
    headers = {"X-Api-Key": api_key, "Content-Type": "application/json"}
    body = json.dumps(data).encode() if data else None
    req = urllib.request.Request(url, data=body, headers=headers, method=method)
    with urllib.request.urlopen(req) as resp:
        return json.loads(resp.read())

def generate_video(api_key, payload):
    return api_request("POST", "/v2/video/generate", api_key, payload)

def check_status(api_key, video_id):
    return api_request("GET", f"/v1/video_status.get?video_id={video_id}", api_key)

def download_video(url, dest):
    req = urllib.request.Request(url)
    with urllib.request.urlopen(req) as resp:
        with open(dest, "wb") as f:
            shutil.copyfileobj(resp, f)

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 generate_dashboard_videos.py <HEYGEN_API_KEY>")
        sys.exit(1)

    api_key = sys.argv[1]

    # Verify key works
    try:
        quota = api_request("GET", "/v2/user/remaining_quota", api_key)
        remaining = quota.get("data", {}).get("remaining_quota", 0)
        print(f"HeyGen quota: {remaining}s remaining")
    except urllib.error.HTTPError as e:
        print(f"API key check failed: {e.code} {e.reason}")
        sys.exit(1)

    with open(SCRIPTS_FILE) as f:
        scripts = json.load(f)

    # Submit all 5 videos
    video_ids = {}
    for script in scripts:
        print(f"\nSubmitting: {script['title']}...")
        try:
            result = generate_video(api_key, script["heygen_payload"])
            vid_id = result.get("data", {}).get("video_id")
            if vid_id:
                video_ids[script["id"]] = {"video_id": vid_id, "title": script["title"]}
                print(f"  Video ID: {vid_id}")
            else:
                print(f"  ERROR: {result}")
        except urllib.error.HTTPError as e:
            print(f"  ERROR: {e.code} {e.reason}")

    if not video_ids:
        print("\nNo videos submitted successfully.")
        sys.exit(1)

    print(f"\n{len(video_ids)} videos submitted. Polling for completion...")

    # Poll until all complete (max 20 min)
    completed = {}
    for attempt in range(60):
        all_done = True
        for script_id, info in video_ids.items():
            if script_id in completed:
                continue
            all_done = False
            try:
                status = check_status(api_key, info["video_id"])
                state = status.get("data", {}).get("status", "unknown")
                if state == "completed":
                    video_url = status["data"].get("video_url", "")
                    duration = status["data"].get("duration", 0)
                    completed[script_id] = {"url": video_url, "duration": duration, **info}
                    print(f"  DONE: {info['title']} ({duration}s)")
                elif state == "failed":
                    err = status.get("data", {}).get("error", "unknown error")
                    print(f"  FAILED: {info['title']} - {err}")
                    completed[script_id] = {"url": None, "error": err, **info}
            except Exception as e:
                pass
        if all_done or len(completed) == len(video_ids):
            break
        time.sleep(20)

    # Download completed videos
    for script_id, info in completed.items():
        if not info.get("url"):
            continue
        vid_dir = os.path.join(OUTPUT_DIR, f"dash-{script_id.split('-',1)[0]}")
        os.makedirs(vid_dir, exist_ok=True)
        dest = os.path.join(vid_dir, "video.mp4")
        print(f"\nDownloading {info['title']} to {dest}...")
        download_video(info["url"], dest)

        # Create viewer page
        html = f"""<!DOCTYPE html>
<html lang="en"><head>
<meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{info['title']} — Girl Gone AI</title>
<style>body{{margin:0;background:#0f1117;display:flex;align-items:center;justify-content:center;min-height:100vh;font-family:sans-serif}}
video{{max-width:100%;max-height:90vh;border-radius:12px;box-shadow:0 8px 32px rgba(0,0,0,.5)}}</style>
</head><body>
<video controls autoplay playsinline><source src="video.mp4" type="video/mp4"></video>
</body></html>"""
        with open(os.path.join(vid_dir, "index.html"), "w") as f:
            f.write(html)

    # Summary
    print(f"\n=== SUMMARY ===")
    success = sum(1 for v in completed.values() if v.get("url"))
    failed = sum(1 for v in completed.values() if not v.get("url"))
    print(f"Completed: {success}, Failed: {failed}, Pending: {len(video_ids) - len(completed)}")

    # Write results
    results_file = os.path.join(OUTPUT_DIR, "dashboard-video-results.json")
    with open(results_file, "w") as f:
        json.dump(completed, f, indent=2)
    print(f"Results saved to {results_file}")

if __name__ == "__main__":
    main()
