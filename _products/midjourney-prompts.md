# Midjourney & AI Art Prompt Pack — 150+ Ready-to-Use Prompts

---

## How to Use This Pack

This pack contains 150+ prompts organized across 8 visual categories. Every prompt is copy-paste ready — replace the bracketed [PLACEHOLDER] variables with your specific details before submitting to your AI image generator.

**Tips for best results:**

1. **Replace every placeholder.** The more specific your subject description, the better the output. "[A woman sitting in a cafe]" produces mediocre results. "[A 30-year-old woman with short dark hair, wearing a cream linen blazer, sitting alone at a marble cafe table with an espresso]" produces stunning results.
2. **Use the full prompt.** Every word is there for a reason. The modifiers at the end control quality, style, and mood. Deleting them will change the output.
3. **Adjust aspect ratios.** Change `--ar` to match your use case: `--ar 1:1` for social media, `--ar 16:9` for presentations, `--ar 2:3` for Pinterest, `--ar 9:16` for Stories/Reels.
4. **Iterate with variations.** Generate 4 images, pick your favorite, then use V1-V4 to create variations of the best one.
5. **Combine prompts.** Mix a subject from one prompt with lighting from another and a style modifier from the reference library.

**Placeholder guide:**

- `[SUBJECT]` — the main subject of the image
- `[SETTING]` — where the scene takes place
- `[MOOD]` — emotional quality (serene, dramatic, playful, mysterious)
- `[COLOR PALETTE]` — dominant colors (warm earth tones, cool blues and grays, monochromatic, etc.)
- `[STYLE REFERENCE]` — artist or photographer name, art movement, or visual style

---

## The Prompt Formula

Every prompt in this pack follows a tested structure that Midjourney weights effectively:

```
[Subject and action] + [Setting/environment] + [Style/medium] + [Lighting] + [Camera/lens] + [Color/mood] + [Quality modifiers] + [Parameters]
```

**Why this order matters:** Midjourney gives highest weight to words at the beginning of the prompt. Subject and action come first. Style and technical modifiers come last, where they influence the overall aesthetic without overriding the core subject.

---

## Style Modifier Reference Library

### Quality & Detail Modifiers
- `highly detailed` — increases fine detail rendering
- `ultra-realistic` — pushes toward photorealism
- `8k resolution` — triggers high-resolution detail rendering
- `intricate details` — fine textures, patterns, small elements
- `masterpiece` — generally increases overall quality
- `professional` — clean, polished output
- `award-winning` — triggers composition and lighting quality

### Lighting Modifiers
- `golden hour lighting` — warm, directional, sunset tones
- `blue hour` — cool twilight tones
- `studio lighting` — clean, controlled, commercial
- `Rembrandt lighting` — dramatic portrait lighting with triangle shadow
- `rim lighting` — glowing outline, separates subject from background
- `soft diffused light` — even, flattering, no harsh shadows
- `dramatic chiaroscuro` — high contrast light and dark
- `volumetric lighting` — visible light rays, atmospheric depth
- `backlighting` — subject silhouetted or glowing from behind
- `neon lighting` — cyberpunk, urban, colorful glow
- `overcast flat light` — muted, even, documentary feel
- `candlelight` — warm, intimate, low-key
- `harsh midday sun` — strong shadows, high contrast

### Camera & Lens Modifiers
- `shot on Hasselblad X2D` — medium format, high-end editorial
- `shot on Canon EOS R5` — professional digital photography
- `shot on Leica M11` — classic street photography feel
- `shot on Fujifilm X-T5` — distinctive color rendering
- `85mm f/1.4` — portrait lens, beautiful bokeh
- `35mm f/1.8` — environmental portrait, wider context
- `24mm wide angle` — dramatic perspective, environmental
- `100mm macro` — extreme close-up, detail shots
- `50mm f/1.2` — classic, natural perspective
- `tilt-shift` — miniature effect, selective focus
- `fish-eye lens` — extreme wide, distorted perspective

### Film Stock Emulations
- `Kodak Portra 400` — warm, muted, skin-friendly
- `Kodak Portra 800` — warmer, grainier, editorial
- `Fujifilm Pro 400H` — pastel, soft, airy
- `Kodak Ektar 100` — vivid, saturated, fine grain
- `Ilford HP5` — classic black and white, medium contrast
- `Kodak Tri-X 400` — gritty black and white, high contrast
- `Cinestill 800T` — tungsten-balanced, halation glow, cinematic

### Art Style References
- `in the style of Studio Ghibli` — anime, pastoral, warm
- `in the style of Wes Anderson` — symmetrical, pastel, quirky
- `in the style of Blade Runner` — dystopian, neon, rain-soaked
- `Art Nouveau style` — organic, ornate, flowing lines
- `Art Deco style` — geometric, metallic, glamorous
- `Bauhaus style` — minimal, geometric, primary colors
- `ukiyo-e style` — Japanese woodblock print
- `vintage travel poster style` — bold, graphic, retro
- `Soviet propaganda poster style` — bold, red, graphic
- `psychedelic 1960s style` — swirling, vivid, kaleidoscopic

---

## Aspect Ratio Quick Reference

| Use Case | Aspect Ratio | Parameter |
|---|---|---|
| Instagram Post | 1:1 | `--ar 1:1` |
| Instagram Story / TikTok / Reels | 9:16 | `--ar 9:16` |
| Twitter / Facebook Post | 16:9 | `--ar 16:9` |
| Pinterest Pin | 2:3 | `--ar 2:3` |
| YouTube Thumbnail | 16:9 | `--ar 16:9` |
| Blog Header | 3:1 | `--ar 3:1` |
| Desktop Wallpaper | 16:9 | `--ar 16:9` |
| Phone Wallpaper | 9:16 | `--ar 9:16` |
| Book Cover | 2:3 | `--ar 2:3` |
| Product Listing (Square) | 1:1 | `--ar 1:1` |
| Presentation Slide | 16:9 | `--ar 16:9` |
| Print (Standard) | 3:2 | `--ar 3:2` |
| Ultrawide / Panorama | 21:9 | `--ar 21:9` |
| Portrait (Classic) | 4:5 | `--ar 4:5` |

---

## Negative Prompt Cheat Sheet

Use `--no` to exclude common unwanted elements:

```
--no text, watermark, signature, logo, words, letters, blurry, out of focus, low quality, distorted, deformed, ugly, extra limbs, extra fingers, disfigured, bad anatomy, cropped, frame, border
```

**Category-specific negatives:**

- **Portraits:** `--no cartoon, anime, 3d render, mannequin, plastic, uncanny valley`
- **Product Photography:** `--no people, hands, watermark, text overlay, busy background`
- **Food Photography:** `--no artificial, plastic, unappetizing, fast food`
- **Architecture:** `--no people, cars, clutter, construction, scaffolding`
- **Logo Design:** `--no photorealistic, gradient, shadow, 3d, complex background`

---

## Parameter Settings Guide

| Parameter | What It Does | Recommended Range |
|---|---|---|
| `--stylize` or `--s` | Controls artistic interpretation (higher = more stylized) | 50-250 for photorealism, 500-750 for artistic |
| `--chaos` or `--c` | Controls variation between the 4 generated images | 0-20 for consistency, 50-100 for exploration |
| `--quality` or `--q` | Rendering quality/time | 1 (standard), 2 (higher quality, more GPU) |
| `--v 6` | Model version | Use latest available version |
| `--niji 6` | Anime/illustration model | Use for anime, manga, and illustration styles |
| `--tile` | Creates seamless tileable patterns | Use for backgrounds and textures |
| `--weird` or `--w` | Adds unexpected, experimental elements | 0-100 for subtle, 250+ for wild |

---

## Category 1: Photorealistic Photography (25 Prompts)

### 1. Editorial Portrait — Studio

```
Editorial portrait of [SUBJECT DESCRIPTION: e.g., "a 35-year-old man with silver-streaked beard, wearing a charcoal wool turtleneck"], shot on Hasselblad X2D 100C, 80mm f/1.9 lens, shallow depth of field, studio environment with seamless gray backdrop, Rembrandt lighting with soft fill, Kodak Portra 800 film emulation, muted earth tones with warm highlights, editorial fashion magazine style, highly detailed skin texture, natural expression, professional retouching --ar 4:5 --s 150 --no cartoon, illustration, anime
```

### 2. Editorial Portrait — Environmental

```
Environmental portrait of [SUBJECT DESCRIPTION] in [SETTING: e.g., "a sun-drenched ceramics studio"], shot on Canon EOS R5, 35mm f/1.4 lens, natural window light from camera left, subject in their element surrounded by [RELEVANT PROPS], authentic and candid moment, editorial documentary style, warm color grading, visible texture and grain, Kodak Portra 400 emulation, shallow depth of field with environment context --ar 3:2 --s 100 --no posed, stock photo, artificial
```

### 3. Dramatic Low-Key Portrait

```
Dramatic low-key portrait of [SUBJECT DESCRIPTION], single hard light source from above camera right creating deep shadows, dark background falling to pure black, visible only from the light — contours of face, shoulders, and one hand, high contrast chiaroscuro, shot on Leica M11 Monochrom, 50mm f/1.2 Noctilux, Ilford HP5 black and white film grain, emotional intensity, fine art photography --ar 4:5 --s 200 --no color, bright, cheerful, flat lighting
```

### 4. Golden Hour Landscape

```
Sweeping landscape of [SETTING: e.g., "rolling Tuscan hills with cypress trees lining a winding gravel road"], golden hour, the sun just above the horizon casting long warm shadows across the terrain, dramatic cloud formations catching orange and pink light, shot on Fujifilm GFX 100S, 32-64mm zoom lens at f/8, deep depth of field, vivid but natural color saturation, Kodak Ektar 100 film emulation, epic scale with foreground interest, landscape photography award winner --ar 16:9 --s 150
```

### 5. Street Photography — Urban

```
Candid street photography moment in [CITY], [SUBJECT: e.g., "an elderly man reading a newspaper on a park bench, pigeons at his feet"], shot on Leica M11, 35mm Summicron f/2, natural overcast light, urban environment with architectural context, decisive moment composition, Kodak Tri-X 400 black and white film grain, documentary style, slightly underexposed for mood, authentic and unposed --ar 3:2 --s 50 --no color, staged, posed, studio
```

### 6. Commercial Lifestyle

```
Lifestyle photography of [SUBJECT: e.g., "a young couple cooking together in a bright, modern kitchen"], natural and relaxed interaction, genuine laughter, shot on Sony A7IV, 50mm f/1.4, soft natural window light supplemented with a subtle bounce fill, warm contemporary color palette, clean and airy aesthetic, commercial brand photography style, catalog quality, relatable and aspirational --ar 16:9 --s 100 --no dark, moody, dramatic, artificial
```

### 7. Macro Close-Up — Nature

```
Extreme macro photography of [SUBJECT: e.g., "morning dew drops on a spider web, each droplet reflecting the sunrise"], shot on Canon EOS R5 with MP-E 65mm macro lens, 5:1 magnification, razor-thin depth of field, backlit by early morning sun creating prismatic light effects in the water droplets, vibrant natural colors, visible surface textures at microscopic scale, National Geographic quality --ar 3:2 --s 200
```

### 8. Moody Cinematic Portrait

```
Cinematic portrait of [SUBJECT DESCRIPTION], moody atmospheric lighting, [SETTING: e.g., "standing in a rain-soaked alley at night, neon signs reflecting in puddles"], Cinestill 800T film emulation with characteristic halation glow around highlights, shot on Arri Alexa Mini with anamorphic lens, 2.39:1 aspect ratio, teal and orange color grading, shallow depth of field, atmospheric fog or rain, film still quality --ar 21:9 --s 250
```

### 9. Product Lifestyle — Flat Lay

```
Overhead flat lay photograph of [PRODUCT: e.g., "a leather-bound journal, vintage fountain pen, brass compass, and dried eucalyptus sprigs"], arranged on [SURFACE: e.g., "weathered dark oak table"], soft directional natural light from the top of frame, carefully styled with negative space for text, muted earth-tone color palette, editorial still life, shot on Fujifilm X-T5, 23mm f/2, warm film tone --ar 1:1 --s 100 --no people, hands, clutter
```

### 10. Headshot — Professional

```
Professional headshot of [SUBJECT DESCRIPTION], clean studio setup with softbox key light at 45 degrees and white reflector fill, neutral gray backdrop with subtle gradient, shot on Canon EOS R5, 85mm f/1.4, eyes tack sharp, gentle depth of field blur on ears and shoulders, natural and approachable expression, corporate headshot quality, clean retouching, neutral color temperature --ar 4:5 --s 50 --no dramatic, moody, artistic, heavy filter
```

### 11. Aerial / Drone Photography

```
Aerial drone photography of [SUBJECT: e.g., "a winding river cutting through autumn forest, the canopy a patchwork of red, orange, and gold"], shot from 200 feet directly above, bird's-eye perspective revealing natural patterns and textures, golden hour side light creating long shadows, shot on DJI Mavic 3 Hasselblad camera, vivid natural colors, epic landscape scale, National Geographic aerial photography --ar 16:9 --s 150
```

### 12. Night Photography — Long Exposure

```
Long exposure night photography of [SUBJECT: e.g., "a coastal lighthouse on a rocky cliff, Milky Way galaxy visible overhead"], 30-second exposure, star trails or sharp star points, smooth silky water from long exposure, light from the lighthouse beam cutting through sea mist, shot on Sony A7S III, 14mm f/1.8, tripod-mounted, deep blue and violet tones with warm lighthouse light, astrophotography quality --ar 16:9 --s 200
```

### 13. Fashion Editorial — Outdoor

```
High fashion editorial photograph of [SUBJECT: e.g., "a model in a flowing crimson silk gown"], [SETTING: e.g., "standing on a windswept sand dune at sunset"], fabric billowing dramatically in the wind, shot on Phase One IQ4 150MP, 110mm f/2.8, golden hour backlight creating a halo effect, warm honey tones, Vogue editorial quality, dynamic and elegant pose, fashion magazine cover composition --ar 2:3 --s 250
```

### 14. Documentary / Photojournalism

```
Documentary-style photograph of [SUBJECT: e.g., "artisan hands shaping wet clay on a spinning pottery wheel"], tight crop on the hands and the work, available light from a nearby window, shallow depth of field isolating the point of action, Kodak Tri-X 400 tonal quality, storytelling through detail, authentic and unpolished, raw emotional connection to craft, photojournalism style --ar 3:2 --s 50
```

### 15. Architecture — Interior

```
Interior architecture photograph of [SPACE: e.g., "a minimalist Japanese tea room with tatami mats, shoji screens, and a single ikebana arrangement"], natural light filtering through translucent screens, clean geometric lines, negative space as a design element, shot on Canon TS-E 24mm tilt-shift lens, corrected verticals, warm neutral palette, Architectural Digest quality, serene and contemplative atmosphere --ar 16:9 --s 100
```

### 16. Portrait — Natural Light Window

```
Natural light portrait of [SUBJECT DESCRIPTION] positioned near a large north-facing window, soft wraparound light with gentle falloff into shadow on the far side, [SETTING: e.g., "minimalist white-walled room with a single wooden chair"], shot on Nikon Z9, 58mm f/0.95 Noct, extremely shallow depth of field, dreamy bokeh, Fujifilm Pro 400H film emulation, pastel and airy, ethereal quality --ar 4:5 --s 150
```

### 17. Food Photography — Hero Shot

```
Hero food photograph of [DISH: e.g., "a towering gourmet burger with melted aged cheddar, caramelized onions, and a brioche bun, cut in half revealing layers"], shot at 45-degree angle on [SURFACE: e.g., "black slate board with parchment paper"], three-point lighting with warm key from camera left, soft fill, and rim light highlighting steam, shallow depth of field on the cut face, Bon Appetit magazine quality, mouth-watering food styling --ar 4:5 --s 150
```

### 18. Sports / Action

```
Dynamic action photograph of [SUBJECT: e.g., "a surfer inside a massive turquoise barrel wave, spray arcing overhead"], frozen motion at 1/4000 shutter speed, shot on Canon EOS R3, 400mm f/2.8 telephoto, compressed perspective, dramatic backlight through the wave, water droplets frozen in air, vivid color saturation, Sports Illustrated cover quality, peak action moment --ar 16:9 --s 100
```

### 19. Portrait — Film Noir Style

```
Film noir style portrait of [SUBJECT DESCRIPTION], dramatic venetian blind shadows falling across the face, single hard light source from camera right, deep shadows, high contrast black and white, cigarette smoke or atmospheric haze, 1940s aesthetic, shot on Leica M6, Ilford HP5 pushed to 1600, visible grain, moody and mysterious, cinematic composition --ar 4:5 --s 200 --no color, modern, cheerful
```

### 20. Autumn / Seasonal Landscape

```
[SEASON] landscape photograph of [SETTING: e.g., "a covered wooden bridge over a gentle stream, surrounded by maple trees in peak fall foliage"], early morning mist rising from the water, warm directional light filtering through the canopy, vibrant [SEASON-APPROPRIATE COLORS: e.g., "red, orange, and gold leaves"], shot on Hasselblad X2D, 45mm f/3.5, medium format depth and detail, saturated but natural color, calendar-quality landscape --ar 3:2 --s 150
```

### 21. Cozy / Hygge Still Life

```
Warm cozy still life photograph of [SUBJECT: e.g., "a steaming mug of coffee beside an open book, chunky knit blanket, and a flickering candle"], [SETTING: e.g., "rain-streaked window in the background with soft bokeh city lights"], warm tungsten color temperature, shallow depth of field centered on the mug's steam, tactile textures — knit, ceramic, paper, candlelight glow, Fujifilm X-T5 Classic Negative film simulation, intimate and inviting --ar 1:1 --s 150
```

### 22. Pet / Animal Portrait

```
Studio portrait of [ANIMAL: e.g., "a regal Great Dane with a brindle coat"], dark charcoal backdrop, single large softbox key light from 45 degrees creating catch lights in the eyes, shallow depth of field, tack-sharp focus on the eyes, visible fur texture, dignified pose, shot on Nikon Z9, 105mm f/1.4, professional pet photography, warmth and personality captured --ar 4:5 --s 100
```

### 23. Travel Photography — Iconic Location

```
Travel photograph of [LOCATION: e.g., "Santorini, Greece — blue-domed churches overlooking the Aegean Sea at sunset"], golden hour light painting the white buildings warm, deep blue water contrasting with warm white and terracotta architecture, human element for scale [e.g., "a solo traveler in a white sundress walking up stone steps"], shot on Sony A7CR, 24-70mm f/2.8, rich vivid colors, wanderlust aesthetic, National Geographic Traveler quality --ar 3:2 --s 150
```

### 24. Minimalist Product — White Background

```
Product photography of [PRODUCT: e.g., "a sleek matte black wireless earbud case, slightly open revealing one earbud"], centered on pure white infinity background, soft even studio lighting with no harsh shadows, subtle ground shadow for dimension, clean and minimal, shot on Canon EOS R5, 100mm macro f/2.8, tack-sharp focus, commercial e-commerce quality, Amazon/Apple product listing style --ar 1:1 --s 50 --no people, props, text, watermark, busy background
```

### 25. Double Exposure / Creative

```
Double exposure photograph combining [SUBJECT 1: e.g., "a woman's profile silhouette"] with [SUBJECT 2: e.g., "a dense forest of redwood trees"], the trees filling the silhouette while the face outline remains clearly defined, artistic blend of human form and nature, muted green and earth tones, shot on analog camera with in-camera double exposure technique, fine art photography, dreamlike and surreal, gallery quality --ar 4:5 --s 300
```

---

## Category 2: Illustration & Digital Art (20 Prompts)

### 26. Children's Book Illustration

```
Children's book illustration of [SCENE: e.g., "a small fox wearing a red scarf, sitting on a mushroom in an enchanted forest, reading a tiny book by lantern light"], watercolor and ink style, soft warm palette with [COLORS: e.g., "amber, sage green, and cream"], gentle linework, whimsical and cozy atmosphere, visible paper texture, storybook quality, reminiscent of classic children's illustration, Caldecott Medal quality --ar 3:2 --s 400 --niji 6
```

### 27. Editorial Illustration — Magazine

```
Editorial illustration for a magazine article about [TOPIC: e.g., "the loneliness of remote work"], conceptual and metaphorical, [VISUAL METAPHOR: e.g., "a person sitting inside a snow globe on an empty desk"], limited color palette — [COLORS: e.g., "muted blue, warm yellow, and white"], flat shapes with subtle texture, clean composition with space for text overlay, New Yorker / Atlantic magazine illustration style --ar 3:4 --s 500
```

### 28. Comic / Graphic Novel Panel

```
Comic book panel illustration of [SCENE: e.g., "a detective in a trenchcoat pushing open the door of a dimly lit jazz club, silhouettes visible through cigarette smoke"], dynamic perspective with dramatic foreshortening, bold ink lines with cross-hatching for shadows, limited color palette — [COLORS: e.g., "noir blacks, deep purple, single warm yellow spotlight"], graphic novel quality, cinematic composition, Frank Miller meets Sean Phillips style --ar 2:3 --s 300
```

### 29. Watercolor Botanical

```
Botanical watercolor illustration of [PLANT: e.g., "a blooming peony in three stages — bud, half-open, and full bloom, with detailed leaf and stem studies"], scientific illustration meets fine art, delicate watercolor washes with precise ink line details, cream paper background, visible brushstrokes and water bloom effects, muted natural palette, botanical garden archival print quality, vintage herbarium aesthetic --ar 2:3 --s 400
```

### 30. Flat Vector Design — Tech

```
Flat vector illustration for a [USE CASE: e.g., "SaaS landing page hero section about team collaboration"], isometric or flat perspective, [SCENE: e.g., "diverse team members connected by flowing lines, working on floating screens and devices"], modern tech company style, clean geometric shapes, limited palette of [COLORS: e.g., "coral, teal, warm gray, and white"], no gradients, outlined characters with minimal detail, Slack/Notion/Linear website illustration style --ar 16:9 --s 300
```

### 31. Retro Poster Art

```
Retro travel poster of [LOCATION: e.g., "Tokyo, Japan — cherry blossom season"], 1950s vintage travel poster style, bold flat colors, simplified geometric shapes, dramatic perspective, hand-lettered title text reading "[LOCATION NAME]", limited palette of [COLORS: e.g., "pink, navy, gold, and cream"], visible print texture, Art Deco influence, National Park Service poster aesthetic --ar 2:3 --s 400
```

### 32. Storybook Environment — Fantasy

```
Illustrated fantasy environment of [SETTING: e.g., "a cozy hobbit-like home built into a hillside, with a round green door, flower boxes, and smoke curling from a chimney"], warm inviting atmosphere, lush vegetation, late afternoon light, watercolor and gouache painting style, rich earth tones with pops of color in the flowers and door, detailed but approachable, storybook illustration, Tolkien meets Studio Ghibli --ar 16:9 --s 400
```

### 33. Line Art — Minimalist

```
Minimalist single-line art illustration of [SUBJECT: e.g., "a woman's face in profile, her hair flowing into ocean waves"], continuous line drawing, elegant and flowing, black ink on white background, no shading or fill, abstract where the line suggests rather than defines, gallery-quality fine art print, modern minimalist aesthetic, perfect for framing --ar 1:1 --s 200
```

### 34. Pixel Art — Retro Gaming

```
Pixel art scene of [SETTING: e.g., "a neon-lit cyberpunk ramen shop at night, steam rising, rain falling, a lone customer at the counter"], 16-bit or 32-bit video game aesthetic, vibrant neon colors against dark backgrounds, detailed pixel work, atmospheric lighting with glow effects, nostalgic retro gaming feel, lo-fi and cozy, animated GIF quality --ar 16:9 --s 300
```

### 35. Infographic Illustration

```
Clean infographic illustration showing [CONCEPT: e.g., "the lifecycle of a coffee bean from farm to cup"], step-by-step visual flow, flat illustration style, numbered steps with small detailed vignettes, cohesive color palette of [COLORS: e.g., "coffee brown, cream, sage green, and white"], icons and small illustrations instead of text where possible, modern editorial infographic design --ar 9:16 --s 200
```

### 36. Gouache Painting — Landscape

```
Gouache painting of [LANDSCAPE: e.g., "a Mediterranean coastal village at golden hour, terracotta rooftops cascading down to a turquoise harbor"], visible brushstrokes showing the artist's hand, rich opaque colors layered with confident strokes, warm sunset palette, atmospheric perspective fading into hazy mountains, plein air painting quality, impressionistic detail, gallery-ready fine art --ar 3:2 --s 500
```

### 37. Paper Cut Art

```
Paper cut art illustration of [SCENE: e.g., "a forest scene with layered trees, a deer, and birds in flight"], multi-layered paper cutting effect with visible depth between layers, subtle shadows between paper layers, [COLORS: e.g., "forest green, moss, cream, and gold"] craft paper textures, intricate cut details in foliage and animal silhouettes, handcrafted aesthetic, shadow box art quality --ar 1:1 --s 400
```

### 38. Risograph Print Style

```
Risograph print illustration of [SUBJECT: e.g., "a cat sleeping in a sunbeam on a stack of books"], limited color separation — [COLORS: e.g., "fluorescent pink and teal with overlapping areas creating a third color"], visible halftone dot pattern, slight misregistration between color layers, textured paper background, indie zine aesthetic, charming imperfections, modern printmaking style --ar 1:1 --s 300
```

### 39. Anatomical / Scientific Illustration

```
Detailed scientific illustration of [SUBJECT: e.g., "a human heart, anatomically accurate, showing chambers, valves, and major vessels"], medical illustration style with precise rendering, colored pencil and ink on cream paper, labeled anatomical features, cross-section view revealing interior structure, Gray's Anatomy meets modern medical illustration, educational and beautiful, museum-quality print --ar 3:4 --s 200
```

### 40. Character Design — Turnaround

```
Character design turnaround sheet for [CHARACTER: e.g., "a young female alchemist with copper goggles, leather apron, and wild curly hair"], front view, 3/4 view, and side view on white background, consistent proportions and details across all angles, color callout swatches, equipment/accessory detail close-ups, animation or game-ready character sheet, clean linework with flat color fills --ar 16:9 --s 200
```

### 41. Woodcut Print

```
Woodcut print illustration of [SUBJECT: e.g., "a stormy sea with a small fishing boat being tossed by enormous waves"], bold black and white with strong contrast, visible wood grain texture in the carved lines, dramatic composition inspired by Hokusai, hand-printed aesthetic, limited detail suggesting form through bold marks, traditional Japanese woodblock printing meets Western linocut --ar 3:2 --s 400
```

### 42. Map Illustration — Fantasy

```
Illustrated fantasy map of [PLACE: e.g., "a fictional island kingdom with mountains, forests, a walled city, coastal villages, and a dragon's lair"], hand-drawn cartography style, parchment paper background, mountain ranges shown in elevation, tiny illustrated trees for forests, compass rose in the corner, decorative border, Tolkien map meets vintage nautical chart, warm sepia and ink tones --ar 4:3 --s 300
```

### 43. Collage Art — Mixed Media

```
Mixed media collage artwork about [THEME: e.g., "the passage of time and memory"], combining vintage photographs, botanical illustrations, handwritten text fragments, postage stamps, fabric textures, and paint splatters, layered composition with depth, [COLOR PALETTE: e.g., "faded earth tones with pops of cobalt blue"], surreal juxtaposition, contemporary art gallery quality --ar 1:1 --s 500
```

### 44. Art Nouveau Poster

```
Art Nouveau poster illustration of [SUBJECT: e.g., "a woman surrounded by flowing iris flowers"], Alphonse Mucha style, ornate decorative border with organic flowing lines, figure integrated with botanical elements, limited palette of [COLORS: e.g., "gold, sage green, dusty rose, and cream"], flat areas of color with delicate linework, lithograph print texture, Belle Epoque aesthetic --ar 2:3 --s 500
```

### 45. Isometric Scene

```
Isometric illustration of [SCENE: e.g., "a cozy apartment cross-section showing living room, kitchen, bedroom, and bathroom"], cute and detailed, each room filled with tiny props and furniture, warm color palette, clean geometric shapes, no outlines — color blocks only, pixel-perfect alignment, game asset quality, charming and inviting, cross-section dollhouse aesthetic --ar 1:1 --s 200
```

---

## Category 3: Concept Art & Fantasy (20 Prompts)

### 46. Character Design — Full Body

```
Full-body character concept art of [CHARACTER: e.g., "a battle-scarred orc chieftain with tribal war paint, bone armor, a massive war hammer, and a wolf-pelt cloak"], dynamic 3/4 stance, dramatic lighting from below, detailed material rendering — metal, leather, bone, fur, dark fantasy palette with muted earth tones and one accent color [e.g., "blood red war paint"], white background, AAA game studio quality, concept art by --ar 2:3 --s 200
```

### 47. Environment Concept — Exterior

```
Environment concept art of [SETTING: e.g., "an ancient elven city built into the canopy of colossal trees, connected by rope bridges and spiral staircases carved into living wood"], sweeping establishing shot, atmospheric perspective with morning mist in the lower canopy, dappled sunlight filtering through leaves above, bioluminescent plants providing accent lighting, epic scale with tiny figures for reference, Weta Workshop meets Lord of the Rings, cinematic composition --ar 21:9 --s 250
```

### 48. Creature Design

```
Creature concept art of [CREATURE: e.g., "a deep-sea leviathan — bioluminescent, serpentine body, armored scales, multiple rows of translucent fins, eyeless head with sonar-sensing organs"], anatomically plausible, turnaround showing front, side, and detail callouts of head and fin structure, size comparison chart with human figure, natural history illustration meets sci-fi creature design, dark oceanic color palette with bioluminescent blue accents --ar 16:9 --s 200
```

### 49. Weapon / Prop Design

```
Prop concept art sheet for [ITEM: e.g., "an ancient enchanted sword — the blade made of crystallized starlight, the crossguard shaped like dragon wings, the grip wrapped in midnight-blue leather, runes glowing along the fuller"], multiple angles — sheathed, drawn, and detail close-ups of the guard, pommel, and blade runes, clean white background, material callouts, scale reference, game-ready prop design --ar 16:9 --s 150
```

### 50. Sci-Fi Cityscape

```
Futuristic cityscape concept art of [SETTING: e.g., "a vertical megacity built on floating platforms above toxic clouds, connected by light bridges, with flying vehicles threading between massive tower structures"], looking up from street level, atmospheric perspective, neon signage in [LANGUAGE], volumetric lighting from advertisements and vehicle headlights, Blade Runner meets The Fifth Element, rain-slicked surfaces reflecting neon, cinematic establishing shot --ar 21:9 --s 300
```

### 51. Fantasy Landscape — Epic

```
Epic fantasy landscape of [SETTING: e.g., "a shattered mountain range where a god fell — the impact crater now a vast lake, fragments of divine armor scattered across the peaks, a pilgrimage road winding up to the crater's edge"], dramatic scale, tiny caravan on the road for size reference, storm clouds breaking to reveal divine light, painted in oils, rich saturated colors, concept art for a AAA game cinematic, awe-inspiring and ancient --ar 21:9 --s 300
```

### 52. Interior Concept — Dungeon/Cave

```
Interior environment concept art of [SPACE: e.g., "an underground dwarven forge, massive stone pillars carved with runes, rivers of molten metal flowing through stone channels, enormous anvil at center, heat haze distorting the air"], warm orange and red lighting from the molten metal, cool blue-gray stone, dramatic chiaroscuro, smoke and sparks, cinematic camera angle looking down into the forge from an elevated walkway --ar 16:9 --s 250
```

### 53. Vehicle / Ship Design

```
Vehicle concept art of [VEHICLE: e.g., "a steampunk airship — wooden hull, brass fittings, multiple canvas sails, steam-powered propeller arrays, observation deck with telescope, cargo nets hanging below"], 3/4 view plus side profile, clean white background, detail callouts for propulsion system and bridge, scale reference with human figures on deck, Victorian engineering meets fantasy adventure, warm brass and wood tones --ar 16:9 --s 200
```

### 54. Character Portrait — Bust

```
Character portrait bust of [CHARACTER: e.g., "an ancient elven queen with silver hair, crown of living branches with tiny flowers, wise and melancholy eyes, fine wrinkles suggesting millennia of life"], shoulders-up composition, Rembrandt lighting, painterly rendering with visible brushstrokes, dark atmospheric background, fantasy realism, oil painting quality, emotional depth and character history visible in the expression --ar 4:5 --s 300
```

### 55. Battle Scene — Dynamic

```
Dynamic battle scene concept art of [SCENE: e.g., "a lone samurai facing a massive serpent dragon in a burning bamboo forest"], action frozen at the peak moment, dramatic diagonal composition, motion blur on secondary elements, ash and embers filling the air, moonlight cutting through smoke, red and orange fire contrasting with cool blue moonlight, cinematic camera angle, Japanese ink painting meets modern concept art --ar 16:9 --s 250
```

### 56. Sci-Fi Character — Armor Design

```
Sci-fi character concept art of [CHARACTER: e.g., "a female bounty hunter in modular power armor, helmet retracted showing scarred face and cybernetic eye implant"], front view with armor callout annotations, glowing energy lines tracing the armor seams in [COLOR: e.g., "cyan"], weathered and battle-damaged armor surface, hard surface sci-fi design, Mass Effect meets Mandalorian aesthetic, white background, game-ready character design --ar 2:3 --s 150
```

### 57. Magical Effect / Spell Design

```
Concept art of [MAGICAL EFFECT: e.g., "a time-stop spell — reality fracturing into crystalline shards around the caster, each shard showing a different moment frozen in time, golden temporal energy spiraling outward"], VFX concept for film or game, dramatic lighting from the spell itself, dark environment to showcase the effect, particle effects and energy trails, magical and awe-inspiring, spell effect reference sheet --ar 16:9 --s 300
```

### 58. Post-Apocalyptic Environment

```
Post-apocalyptic environment concept art of [SETTING: e.g., "an abandoned shopping mall reclaimed by nature — trees growing through the skylights, vines covering escalators, a deer drinking from a fountain in the atrium, sunlight streaming through broken glass"], quiet beauty in decay, nature reclaiming civilization, Last of Us aesthetic, warm dappled light contrasting with cold concrete and steel, atmospheric and contemplative --ar 16:9 --s 200
```

### 59. Mecha / Robot Design

```
Mech design concept art of [MECH: e.g., "a 40-foot agricultural mech repurposed for combat, original farm equipment visible under welded-on armor plates, a grain silo shield, and a hydraulic arm converted to a weapon mount"], standing in [SETTING: e.g., "a wheat field"], utilitarian and improvised aesthetic, rust and weathering, scale reference with human pilot visible in the open cockpit, diesel punk meets Pacific Rim, functional and believable --ar 2:3 --s 200
```

### 60. Underwater Scene

```
Underwater concept art of [SCENE: e.g., "a sunken cathedral on the ocean floor, coral growing on gothic arches, schools of tropical fish swimming through stained glass windows, bioluminescent jellyfish drifting through the nave"], god rays filtering down from the surface, deep blue water gradient, warm bioluminescent accents, mysterious and sacred atmosphere, Jacques Cousteau meets fantasy, rich color and atmosphere --ar 16:9 --s 300
```

### 61. Steampunk Interior

```
Steampunk interior concept art of [SPACE: e.g., "an inventor's workshop — walls covered in brass gears and pipes, a workbench cluttered with half-finished automatons, blueprints pinned everywhere, a small steam engine powering overhead belt drives"], warm gas lamp lighting, visible steam and brass reflections, cluttered but organized chaos, rich warm color palette, detail-rich environment, Victorian science fiction --ar 16:9 --s 250
```

### 62. Dark Fantasy — Horror

```
Dark fantasy horror concept art of [SUBJECT: e.g., "an eldritch entity emerging from a portal in a medieval library — tentacles of liquid shadow pulling books from shelves, a terrified scholar backing away, reality distorting around the breach"], Lovecraftian horror, impossible geometry near the portal, dramatic chiaroscuro with the entity absorbing light, cold desaturated palette with sickly green accents from the portal, Beksinski meets Dark Souls --ar 16:9 --s 300
```

### 63. Space Station Interior

```
Sci-fi space station interior concept art of [SPACE: e.g., "the observation deck — a massive curved window looking out at a gas giant, minimalist furniture, holographic displays floating in the air, a single astronaut in casual clothing gazing out"], clean futuristic design, soft ambient lighting from the planet glow, near-future plausible technology, The Expanse meets 2001: A Space Odyssey, contemplative atmosphere, hard sci-fi aesthetic --ar 21:9 --s 200
```

### 64. Mythological Scene

```
Concept art of [MYTHOLOGICAL SCENE: e.g., "Icarus moments before the fall — too close to the sun, wax wings beginning to melt, feathers scattering behind him, the tiny island of Crete far below in a wine-dark sea"], classical mythology meets modern concept art, dramatic upward angle, golden sunlight overwhelming the top of frame, figure in silhouette against the sun, Renaissance painting composition with contemporary rendering, tragic and beautiful --ar 2:3 --s 400
```

### 65. Alien Planet Landscape

```
Alien planet landscape concept art of [SETTING: e.g., "a world with crystalline vegetation — trees of purple quartz, grass made of fine glass filaments that chime in the wind, twin suns setting on the horizon, an exploration team in environmental suits collecting samples"], otherworldly but plausible, bioluminescence activating as the suns set, unfamiliar color palette — [COLORS: e.g., "violet, amber, and magenta"], scientific exploration meets wonder, hard sci-fi aesthetic --ar 21:9 --s 300
```

---

## Category 4: Logo & Brand Design (15 Prompts)

### 66. Minimalist Logo Mark

```
Minimalist logo mark for [BRAND: e.g., "a sustainable coffee company called 'Rooted'"], abstract geometric symbol combining [ELEMENTS: e.g., "a coffee bean and a tree root"], clean vector lines, single color — [COLOR: e.g., "deep forest green"], works at all sizes from favicon to billboard, modern and timeless, white background, no text, no gradients, professional brand identity design --ar 1:1 --s 100 --no photorealistic, 3d, shadow, complex, detailed, gradient, text
```

### 67. Mascot Logo

```
Mascot logo character for [BRAND: e.g., "a kids' coding academy called 'ByteBuddy'"], [CHARACTER: e.g., "a friendly robot with a lightbulb head, wearing sneakers, giving a thumbs up"], cartoon style, bold outlines, limited flat color palette — [COLORS: e.g., "electric blue, bright yellow, and white"], expressive and approachable, works as a standalone icon, clean white background, esports/modern mascot style --ar 1:1 --s 200 --no realistic, scary, complex background
```

### 68. Wordmark Logo

```
Custom wordmark logo for [BRAND NAME: e.g., "NOVA"], elegant typography with [STYLE: e.g., "a custom sans-serif where the O contains a subtle star/sparkle element"], single weight, tracking adjusted for visual balance, [COLOR: e.g., "midnight navy on white background"], modern and premium feel, fashion/luxury brand aesthetic, works in horizontal lockup, no additional symbols or marks --ar 3:1 --s 100 --no photorealistic, 3d, shadow, illustration
```

### 69. Emblem / Badge Logo

```
Emblem badge logo for [BRAND: e.g., "a craft brewery called 'Iron Creek Brewing Co., est. 2024'"], circular badge design with [ELEMENTS: e.g., "mountain silhouette, wheat stalks, a creek flowing through"], banner text with establishment year, vintage/heritage feel, limited color palette — [COLORS: e.g., "copper, cream, and dark brown"], detailed but clean at small sizes, stamp or label aesthetic, craft brand identity --ar 1:1 --s 200 --no photorealistic, 3d, modern
```

### 70. App Icon

```
Mobile app icon for [APP: e.g., "a meditation and breathing app called 'Breathe'"], [VISUAL: e.g., "abstract representation of a breath — soft organic curve suggesting inhalation, gradient from calm blue to serene lavender"], rounded square format (iOS style), simple enough to read at 60x60 pixels, single focal element, modern and calming, flat design with one subtle gradient, clean and recognizable --ar 1:1 --s 100 --no text, complex, detailed, realistic, 3d
```

### 71. Monogram Logo

```
Monogram logo combining the letters [LETTERS: e.g., "A and M"] for [BRAND: e.g., "a luxury architecture firm"], letters interlocked or overlapping in a balanced geometric composition, [STYLE: e.g., "modern geometric with thin elegant lines"], single color — [COLOR: e.g., "black on white background"], timeless and premium, works embossed on stationery and etched on glass, luxury brand identity --ar 1:1 --s 100 --no playful, cartoon, colorful, gradient
```

### 72. Hand-Lettered Logo

```
Hand-lettered logo for [BRAND: e.g., "a bakery called 'The Rolling Pin'"], custom brush script lettering with natural flow and variation, [STYLE: e.g., "confident brush strokes with a vintage feel"], [COLOR: e.g., "warm terracotta on cream"], authentic handcrafted aesthetic, slight texture in the strokes, artisanal and warm, bakery/cafe brand identity, single color for versatility --ar 3:1 --s 200 --no digital, clean, geometric, sans-serif
```

### 73. Geometric Abstract Logo

```
Geometric abstract logo for [BRAND: e.g., "a fintech startup called 'Prism'"], [CONCEPT: e.g., "triangular prism shape that subtly contains an upward arrow, suggesting growth and clarity"], [COLORS: e.g., "gradient from deep blue to electric cyan"], clean vector shapes, mathematical precision, modern tech company aesthetic, works in full color and single-color variants, Silicon Valley startup identity --ar 1:1 --s 100 --no organic, handdrawn, vintage, complex
```

### 74. Vintage / Retro Logo

```
Vintage-style logo for [BRAND: e.g., "a barbershop called 'The Gentleman's Cut, est. 2024'"], [STYLE: e.g., "1920s/Art Deco inspired with geometric borders, decorative lines, and classic serif typography"], [COLORS: e.g., "gold and black"], ornate but readable, detailed border work, old-fashioned craftsmanship, works on a sign, business card, and social media, heritage brand identity --ar 1:1 --s 300 --no modern, minimal, colorful, photorealistic
```

### 75. Nature-Inspired Logo

```
Nature-inspired logo for [BRAND: e.g., "an outdoor adventure company called 'Summit Trail'"], [ELEMENTS: e.g., "mountain peak with a winding trail leading to the summit, a small sun or star at the peak"], clean linework, [COLORS: e.g., "forest green and stone gray"], outdoor/adventure aesthetic, works embroidered on a cap or printed on gear, REI/Patagonia brand family style, white background --ar 1:1 --s 150 --no photorealistic, complex, gradient, 3d
```

### 76. Negative Space Logo

```
Clever negative space logo for [BRAND: e.g., "a delivery service called 'SwiftBox'"], [CONCEPT: e.g., "a box shape where the negative space between two elements creates a hidden arrow suggesting speed and direction"], single color — [COLOR: e.g., "bright orange"], the hidden element should be discoverable but not immediately obvious, FedEx arrow-level cleverness, modern and minimal, white background, professional brand identity --ar 1:1 --s 100 --no complex, detailed, photorealistic, gradient
```

### 77. Tech / SaaS Logo

```
Modern logo for [BRAND: e.g., "an AI analytics platform called 'Cortex'"], [STYLE: e.g., "abstract neural network nodes connected by subtle lines, forming a brain-like shape"], [COLORS: e.g., "gradient from violet to electric blue"], clean and geometric, tech-forward, works as a favicon and on dark backgrounds, Silicon Valley SaaS aesthetic, professional and innovative, data visualization meets brand identity --ar 1:1 --s 100 --no organic, vintage, handdrawn, complex
```

### 78. Sports / Athletic Logo

```
Sports team logo for [TEAM: e.g., "the 'Thunderhawks' — a competitive esports team"], [MASCOT: e.g., "an aggressive hawk with spread wings, lightning bolt incorporated into the wing design"], dynamic and energetic, bold angular shapes, [COLORS: e.g., "electric yellow and dark navy"], aggressive but clean, works on jerseys, social media, and merchandise, professional esports / sports branding, shield or crest shape optional --ar 1:1 --s 200 --no cute, soft, minimal, photorealistic
```

### 79. Wellness / Health Logo

```
Wellness brand logo for [BRAND: e.g., "a yoga studio called 'Lotus Flow'"], [CONCEPT: e.g., "a simplified lotus flower that subtly incorporates a human figure in a yoga pose within the petals"], [COLORS: e.g., "sage green, soft lavender, and warm gold"], organic and balanced, calming aesthetic, works on a studio sign and water bottle, wellness/health industry branding, modern and serene --ar 1:1 --s 150 --no aggressive, angular, dark, complex
```

### 80. Photography / Creative Logo

```
Logo for [BRAND: e.g., "a wedding photographer called 'Claire Monroe Photography'"], [STYLE: e.g., "elegant serif wordmark with a delicate botanical illustration element — a single olive branch curving above the name"], [COLORS: e.g., "warm gold on white"], refined and romantic, editorial aesthetic, works as a watermark on photos and on a business card, fine art photographer branding, clean background --ar 3:1 --s 150 --no bold, tech, modern, geometric
```

---

## Category 5: Product Photography (20 Prompts)

### 81. E-Commerce — White Background

```
Product photography of [PRODUCT: e.g., "a matte black insulated water bottle, 32oz, with minimalist logo"], centered on pure white infinity curve background, soft even studio lighting — two large softboxes at 45 degrees with a bottom fill, no harsh shadows, subtle ground shadow for dimension, multiple angles — front, 3/4, and detail of cap mechanism, Amazon listing quality, clean and professional --ar 1:1 --s 50 --no people, hands, props, text, busy background
```

### 82. Lifestyle Product — In Context

```
Lifestyle product photography of [PRODUCT: e.g., "a premium leather messenger bag"], in natural context — [SETTING: e.g., "carried by a well-dressed man walking through a cobblestone European street, morning light, cafe in background"], shallow depth of field keeping the product sharp, warm natural color grading, aspirational lifestyle aesthetic, editorial quality, the product is the hero but the setting sells the dream --ar 4:5 --s 150
```

### 83. Flat Lay — Organized

```
Organized flat lay product photography of [PRODUCTS: e.g., "a complete men's grooming kit — safety razor, shaving brush, shaving soap, aftershave, comb, and leather dopp bag"], arranged in a precise grid layout on [SURFACE: e.g., "dark charcoal slate"], overhead camera angle, soft even lighting, each item equidistant, minimalist and clean, [COLOR PALETTE: e.g., "chrome, dark wood, cream, and black leather"], editorial catalog quality, brand campaign imagery --ar 1:1 --s 100 --no clutter, messy, casual
```

### 84. Cosmetics / Beauty Product

```
Beauty product photography of [PRODUCT: e.g., "a luxury lipstick in a gold case, cap off showing the rich burgundy color"], [SETTING: e.g., "lying on crushed rose petals on a marble surface"], dramatic lighting — single hard light from above creating sculptural shadows, product gloss and metallic reflections visible, luxurious and sensual, [COLORS: e.g., "gold, burgundy, white marble, and soft pink petals"], Chanel/Dior campaign quality --ar 4:5 --s 200
```

### 85. Tech Product — Floating

```
Product photography of [TECH PRODUCT: e.g., "wireless noise-canceling headphones in matte white"], floating at a dynamic angle against [BACKGROUND: e.g., "a gradient from soft gray to white"], subtle shadow beneath suggesting levitation, clean studio lighting, one accent light creating a highlight edge, product details tack-sharp — stitching, mesh, buttons all visible, Apple-style product reveal, minimal and premium --ar 1:1 --s 100 --no hands, people, table, surface
```

### 86. Food — Overhead Flat Lay

```
Overhead food photography flat lay of [DISH: e.g., "a full weekend brunch spread — pancakes, eggs benedict, avocado toast, fresh fruit, coffee, and orange juice"], arranged on [SURFACE: e.g., "white marble table with linen napkins and matte black plates"], soft natural top light from a window, artful but casual arrangement, hands reaching for food to add life, warm and inviting, Food52 / Bon Appetit editorial quality --ar 1:1 --s 150
```

### 87. Food — Action Shot

```
Dynamic food action photograph of [ACTION: e.g., "honey being drizzled from a wooden dipper onto a stack of golden pancakes, the honey catching the light as it flows in a thin stream"], frozen motion, shallow depth of field focused on the point of drip, warm directional side light, [SURFACE: e.g., "rustic wooden board"], steam rising from the pancakes, visceral and mouth-watering, commercial food advertising quality --ar 4:5 --s 200
```

### 88. Jewelry — Detail Close-Up

```
Macro jewelry photography of [PIECE: e.g., "a diamond engagement ring, round brilliant cut, platinum band, sitting in the velvet groove of an open ring box"], extreme close-up showing facets and light refraction, multiple catch lights in the stone, shallow depth of field, [BACKGROUND: e.g., "soft cream bokeh"], studio lighting with a ring light for even reflections, luxury jeweler marketing quality, sparkling and romantic --ar 1:1 --s 150
```

### 89. Packaging Mockup

```
Product packaging photography of [PACKAGE: e.g., "a kraft paper coffee bag with matte black label, showing the brand logo and roast type"], styled with [PROPS: e.g., "scattered coffee beans, a rustic wooden scoop, and a burlap cloth"], warm studio lighting, artisanal and premium feel, [SURFACE: e.g., "dark wood table"], shallow depth of field, the packaging is the hero, specialty coffee brand aesthetic --ar 4:5 --s 150
```

### 90. Beverage / Cocktail

```
Cocktail photography of [DRINK: e.g., "a classic Negroni in a crystal rocks glass, large ice sphere, orange peel garnish expressed and placed"], [SETTING: e.g., "on a dark marble bar top, moody bar lighting in soft focus behind"], backlit to make the drink glow amber-red, condensation visible on the glass, shallow depth of field, atmospheric and sophisticated, craft cocktail bar marketing quality --ar 4:5 --s 200
```

### 91. Clothing — Flat Lay

```
Flat lay clothing photography of [OUTFIT: e.g., "a complete spring outfit — white linen button-down, tan chinos rolled at the cuff, brown leather belt, white canvas sneakers, and a straw hat"], artfully arranged on [SURFACE: e.g., "light wood floor"], overhead angle, natural window light, each piece positioned as if worn but laid flat, editorial fashion styling, clean and aspirational, e-commerce catalog quality --ar 1:1 --s 100
```

### 92. Skincare Routine — Multiple Products

```
Skincare product lineup photography of [PRODUCTS: e.g., "5 products in a complete skincare routine — cleanser, toner, serum, moisturizer, and SPF — in matching minimalist white bottles with different colored labels"], arranged in order of use, [SETTING: e.g., "clean white bathroom shelf with a small plant and natural light"], soft even lighting, clean and clinical yet warm, dermatologist-recommended aesthetic, The Ordinary / Glossier brand photography style --ar 16:9 --s 100
```

### 93. Book / Journal — Styled

```
Styled book photography of [BOOK/JOURNAL: e.g., "a hardcover book with a linen cover and embossed gold title"], [SETTING: e.g., "on a bedside table with a reading lamp, glasses, and a cup of tea"], warm ambient lighting, cozy and inviting, slightly messy in an intentional way — bookmark ribbon hanging out, shallow depth of field on the book title, editorial lifestyle, bookstagram aesthetic --ar 4:5 --s 150
```

### 94. Candle / Home Fragrance

```
Product photography of [PRODUCT: e.g., "a luxury soy candle in an amber glass jar, lit with a small flame"], [SETTING: e.g., "on a white marble tray with dried flowers and a matchbox"], warm candlelight as the primary light source supplemented by soft fill, atmospheric and cozy, visible wax pool and wick glow, smoke wisps, [MOOD: e.g., "intimate and calming"], luxury home goods marketing --ar 1:1 --s 200
```

### 95. Shoe — Hero Shot

```
Hero product photography of [SHOE: e.g., "a white leather minimalist sneaker, clean lines, minimal branding"], [ANGLE: e.g., "3/4 view from slightly below, showing the profile and sole"], floating or on a reflective surface, gradient background from [COLORS: e.g., "light gray to white"], single dramatic side light highlighting texture and stitching, product is tack-sharp, Nike/Allbirds campaign quality, clean and desirable --ar 4:5 --s 100
```

### 96. Watch — Detail

```
Luxury watch photography of [WATCH: e.g., "a steel dive watch with a dark blue sunburst dial, applied indices, and a ceramic bezel"], [POSITION: e.g., "standing at an angle on its bracelet, crown facing up"], dramatic studio lighting with reflections on polished surfaces, deep depth of field showing every detail, dark background creating drama, Hodinkee editorial quality, horological precision, aspirational and technical --ar 1:1 --s 200
```

### 97. Stationery / Desk Accessories

```
Styled desk flat lay of [PRODUCTS: e.g., "a premium notebook, brass pen, leather desk pad, marble paperweight, and a small succulent"], [SURFACE: e.g., "warm wood desk"], overhead angle, natural light from the upper left, organized but lived-in arrangement, warm neutral palette, productivity and aesthetics combined, Rifle Paper Co. meets Grovemade styling, aspirational workspace --ar 1:1 --s 150
```

### 98. Supplement / Vitamin Bottle

```
Health supplement product photography of [PRODUCT: e.g., "a matte white bottle with clean minimal label, 60-count capsules"], [SETTING: e.g., "surrounded by fresh ingredients that represent the supplement — turmeric root, black pepper, ginger"], clean and clinical but natural, soft studio lighting, white or light background, FDA-compliant aesthetic (no medical claims in visual), wellness brand marketing quality --ar 4:5 --s 100
```

### 99. Sunglasses — Fashion

```
Fashion sunglasses photography of [PRODUCT: e.g., "tortoiseshell acetate sunglasses with green tinted lenses"], [STYLE: e.g., "laid casually on a beach towel with sunscreen, a straw hat, and a paperback book partially visible"], warm natural sunlight, summer lifestyle context, shallow depth of field on the sunglasses, warm golden tones, beach vacation aesthetic, Ray-Ban / Warby Parker campaign quality --ar 16:9 --s 150
```

### 100. Product Splash / Water

```
Dynamic product splash photography of [PRODUCT: e.g., "a can of sparkling water, citrus flavor"], frozen water splash around the product, droplets suspended in air, dynamic and energetic, studio lighting with backlight illuminating the splash, [COLORS: e.g., "cool cyan water against bright citrus yellow can"], high-speed photography effect, commercial beverage advertising, Super Bowl commercial quality --ar 4:5 --s 200
```

---

## Category 6: Architecture & Interior Design (15 Prompts)

### 101. Modern Residential — Exterior

```
Architectural photograph of [BUILDING: e.g., "a modern single-story desert home with floor-to-ceiling glass walls, flat roof with extended overhangs, exposed concrete and warm wood cladding"], [TIME: e.g., "dusk — interior lights glowing warm against a deep blue twilight sky"], landscape integration with native plants, pool reflecting the structure, shot with tilt-shift lens for corrected verticals, Dwell magazine quality, aspirational residential architecture --ar 16:9 --s 150
```

### 102. Interior — Living Room

```
Interior design photograph of [SPACE: e.g., "a Scandinavian-minimalist living room with double-height ceiling, white oak floors, a modular off-white sofa, single statement artwork on the wall, and a sculptural floor lamp"], natural light from large windows, [TIME: e.g., "late afternoon golden hour creating warm rectangles of light on the floor"], clean and curated, livable luxury, Architectural Digest quality, warm and inviting despite the minimalism --ar 16:9 --s 150
```

### 103. Interior — Kitchen

```
Interior design photograph of [KITCHEN: e.g., "a modern farmhouse kitchen with white shaker cabinets, open shelving with ceramics, a large marble island with waterfall edge, brass fixtures, and a statement range hood"], natural light, styled with [PROPS: e.g., "fresh herbs, a cutting board with bread, and a copper kettle"], warm and functional, kitchen of the year quality, lived-in elegance, Joanna Gaines meets contemporary design --ar 16:9 --s 150
```

### 104. Interior — Bedroom

```
Interior design photograph of [BEDROOM: e.g., "a serene master bedroom with linen bedding in muted earth tones, floor-to-ceiling sheer curtains, floating nightstands, and a gallery wall of abstract art"], [LIGHT: e.g., "soft morning light filtering through sheers"], cozy and calm, textural layers — linen, wool, wood, ceramic, inviting and restful, boutique hotel meets curated home, interior design portfolio quality --ar 16:9 --s 150
```

### 105. Retail / Commercial Space

```
Interior photograph of [SPACE: e.g., "a specialty coffee shop with exposed brick walls, terrazzo floors, a long walnut bar with pour-over stations, hanging pendant lights, and living plants"], [ATMOSPHERE: e.g., "morning light, a few customers in soft focus, steam rising from cups"], warm and inviting, third-wave coffee aesthetic, architectural photography with lifestyle feel, commercial interior design portfolio quality --ar 16:9 --s 150
```

### 106. Interior — Bathroom

```
Interior design photograph of [BATHROOM: e.g., "a spa-like bathroom with freestanding soaking tub, floor-to-ceiling Calacatta marble, matte black fixtures, a live-edge wood vanity, and a frameless glass rain shower"], [LIGHT: e.g., "soft ambient lighting with candles around the tub, twilight through a frosted window"], luxurious and serene, hotel spa quality, every material tactile and premium, interior design magazine centerfold --ar 4:5 --s 200
```

### 107. Outdoor Living Space

```
Architectural photograph of [SPACE: e.g., "a covered outdoor living area with a stone fireplace, L-shaped sectional sofa with outdoor cushions, pergola with climbing wisteria, and a view of rolling hills"], [TIME: e.g., "golden hour, fire lit, string lights beginning to glow"], indoor-outdoor living at its finest, warm and inviting, landscape architecture meets furniture design, aspirational outdoor entertaining --ar 16:9 --s 200
```

### 108. Office / Workspace

```
Interior photograph of [WORKSPACE: e.g., "a creative studio office with a 12-foot reclaimed wood communal table, individual task lighting, a wall of pinned sketches and mood boards, exposed ductwork, polished concrete floors"], [ATMOSPHERE: e.g., "focused but relaxed, plants on windowsills, natural light from skylights"], functional creativity, WeWork meets boutique design studio, commercial architecture photography --ar 16:9 --s 100
```

### 109. Historic / Classical Architecture

```
Architectural photograph of [BUILDING: e.g., "a Beaux-Arts public library — grand staircase, marble columns, coffered ceiling with gilt details, reading room with green banker's lamps"], interior shot emphasizing symmetry and grandeur, [LIGHT: e.g., "warm afternoon sun through arched windows creating dramatic light shafts"], architectural preservation, heritage building documentation, Corinthian column detail, shot on large format --ar 16:9 --s 200
```

### 110. Tiny House / Small Space

```
Interior design photograph of [SPACE: e.g., "a 400-square-foot tiny house with clever storage solutions — built-in dining nook that converts to a work desk, lofted bed with reading nook, full kitchen with hidden appliances, and a bathroom with pocket door"], every inch utilized, warm wood tones with white walls to maximize visual space, natural light from strategically placed windows, small-space living inspiration --ar 16:9 --s 150
```

### 111. Japanese Interior

```
Interior photograph of [SPACE: e.g., "a traditional Japanese ryokan room with tatami floors, shoji screens, low chabudai table, zabuton cushions, and an alcove (tokonoma) with a single ikebana arrangement and hanging scroll"], natural materials only — wood, paper, straw, minimal furnishing, [LIGHT: e.g., "soft diffused daylight through paper screens"], wabi-sabi aesthetic, perfect imperfection, serene and meditative --ar 16:9 --s 200
```

### 112. Industrial Loft

```
Interior photograph of [SPACE: e.g., "a converted warehouse loft — exposed brick, steel I-beams, original timber ceiling, polished concrete floor, with modern furniture creating distinct living zones within the open plan"], [ELEMENTS: e.g., "oversized abstract canvas, vintage leather Chesterfield, modern kitchen island with waterfall counter"], industrial meets refined, soaring ceilings with pendant clusters, urban loft lifestyle --ar 16:9 --s 150
```

### 113. Exterior — Night Architecture

```
Night architecture photograph of [BUILDING: e.g., "a glass-walled contemporary museum, the interior galleries visible and glowing warm against the dark sky, reflecting in a still water feature in the courtyard"], blue hour sky transitioning to dark, architectural lighting highlighting structural elements, long exposure smoothing water reflections, dramatic and sculptural, architectural awards photography --ar 16:9 --s 200
```

### 114. Garden / Landscape Design

```
Landscape design photograph of [GARDEN: e.g., "a formal English garden with geometric box hedges, a gravel path leading to a stone fountain, lavender borders, climbing roses on an iron arbor, and a weathered teak bench"], [TIME: e.g., "early morning, dew on leaves, soft diffused light"], lush and maintained, every plant in its place, garden design magazine quality, tranquil and timeless --ar 16:9 --s 200
```

### 115. Staircase — Architectural Detail

```
Architectural detail photograph of [STAIRCASE: e.g., "a helical concrete staircase with no visible supports, floating steps with glass balustrade, viewed from directly below looking up through the spiral"], geometric patterns created by the architecture itself, strong lines and curves, play of light and shadow, abstract quality in architectural form, shot on wide-angle lens, fine art architecture photography --ar 4:5 --s 200
```

---

## Category 7: Fashion Photography (15 Prompts)

### 116. Editorial — Studio

```
High fashion editorial photograph of [SUBJECT: e.g., "a model in a structured ivory blazer with exaggerated shoulders, paired with wide-leg trousers and minimal gold jewelry"], clean white studio background, dramatic side lighting creating sharp shadows, confident and powerful pose, shot on Phase One IQ4, 120mm f/4 macro, tack-sharp textile detail visible, Vogue Italia editorial, bold and modern --ar 2:3 --s 200
```

### 117. Street Style

```
Street style fashion photograph of [SUBJECT: e.g., "a stylish man in an oversized camel overcoat, black turtleneck, tailored gray trousers, and white leather sneakers, carrying a portfolio bag"], walking through [SETTING: e.g., "a tree-lined Parisian boulevard"], candid mid-stride, natural light, shot on Leica M11, 50mm f/1.4, background softly out of focus, effortless style, Paris Fashion Week street style quality --ar 2:3 --s 100
```

### 118. Lookbook — Full Outfit

```
Lookbook photograph of [OUTFIT: e.g., "a casual summer look — linen shirt in soft blue, tan shorts, woven leather sandals, canvas tote bag, and round sunglasses"], model standing in [SETTING: e.g., "a sunlit courtyard with white stucco walls and terracotta pots"], natural relaxed pose, even natural light, clean and commercial, lifestyle brand catalog quality, aspirational but attainable, Everlane/COS brand aesthetic --ar 2:3 --s 100
```

### 119. Accessory Detail Shot

```
Fashion detail photograph of [ACCESSORY: e.g., "a woman's wrist showing a stack of thin gold bangles, a vintage watch, and a braided leather bracelet"], macro-level detail, skin texture and accessory materials tack-sharp, shallow depth of field, warm natural light, minimal background blur, editorial detail insert quality, complements a full-look fashion story, intimate and tactile --ar 1:1 --s 150
```

### 120. Runway-Inspired

```
Runway-inspired fashion photograph of [SUBJECT: e.g., "a model in an avant-garde deconstructed black dress with asymmetric hem and exposed seams"], [SETTING: e.g., "dramatic spotlight on a dark stage"], model walking toward camera with confidence, motion blur in the fabric, dramatic front lighting, fashion week runway photography, Alexander McQueen meets Maison Margiela aesthetic, avant-garde and editorial --ar 2:3 --s 250
```

### 121. Seasonal Collection — Spring/Summer

```
Spring/summer fashion campaign photograph of [SUBJECT: e.g., "a model in a flowing floral midi dress with puff sleeves and straw accessories"], [SETTING: e.g., "a blooming lavender field in Provence at golden hour"], warm and romantic, breeze catching the fabric, natural light, shot on Fujifilm GFX 100S, medium format depth, dreamy bokeh from the lavender, seasonal and aspirational, luxury resort wear campaign --ar 2:3 --s 200
```

### 122. Seasonal Collection — Fall/Winter

```
Fall/winter fashion campaign photograph of [SUBJECT: e.g., "a model in a chunky cable-knit sweater, wool coat, leather boots, and a cashmere scarf"], [SETTING: e.g., "a misty forest path covered in fallen leaves"], warm but moody, breath visible in cold air, rich earth tones — burgundy, camel, forest green, shot on medium format, atmospheric and tactile, you can feel the textures, luxury outerwear campaign quality --ar 2:3 --s 200
```

### 123. Beauty / Close-Up

```
Beauty editorial close-up of [SUBJECT: e.g., "a model with glowing dewy skin, bold graphic eyeliner, and a natural lip"], tight crop from forehead to chin, beauty lighting — ring light plus soft fill for flawless skin, every pore and lash visible in sharp detail, clean skin retouching preserving texture, editorial makeup artistry, shot on Canon EOS R5, 100mm macro f/2.8, NARS / MAC campaign quality --ar 4:5 --s 150
```

### 124. Swimwear / Beach

```
Swimwear fashion photograph of [SUBJECT: e.g., "a model in a one-piece swimsuit with geometric cutouts, walking along the shoreline"], [SETTING: e.g., "a pristine beach at sunrise, waves lapping at ankles, sky in soft pink and gold gradients"], athletic and confident, warm natural golden hour light, shot at a low angle for dynamic perspective, body-positive and aspirational, Sports Illustrated meets editorial fashion --ar 2:3 --s 150
```

### 125. Menswear — Tailored

```
Menswear editorial photograph of [SUBJECT: e.g., "a man in a slim-fit navy suit with a subtle windowpane check, white Oxford shirt open at the collar, brown leather cap-toe shoes"], [SETTING: e.g., "leaning against a vintage sports car, industrial warehouse in background"], confident and relaxed, golden hour rim light, shallow depth of field, GQ / Esquire editorial quality, modern masculinity, sharp tailoring as the focal point --ar 2:3 --s 150
```

### 126. Knitwear / Texture Focus

```
Fashion photograph focused on texture and material of [GARMENT: e.g., "an oversized hand-knit mohair cardigan in dusty rose, every stitch visible"], close-up showing the knit pattern and fiber texture, model partially visible — focus is on the garment, soft natural window light, warm and tactile, you want to reach out and touch it, artisanal craft meets fashion, knitwear brand campaign --ar 4:5 --s 200
```

### 127. Athletic / Sportswear

```
Sportswear fashion photograph of [SUBJECT: e.g., "a female athlete in sleek black performance leggings and a cropped sports bra, mid-stride"], [SETTING: e.g., "on a rooftop with a city skyline at dawn"], dynamic action pose, athletic and powerful, dramatic rim lighting from the rising sun, motion energy, shot at 1/2000 shutter speed freezing movement, Nike / Adidas campaign quality, empowering and aspirational --ar 2:3 --s 150
```

### 128. Jewelry Editorial

```
Fine jewelry editorial photograph of [PIECES: e.g., "a statement gold collar necklace with geometric links, paired with matching ear cuffs"], on [MODEL: e.g., "a model with slicked-back hair and minimal makeup, emphasizing the jewelry"], beauty lighting with focused accent lights creating sparkle and reflection on metal surfaces, clean dark background, luxury and artistry, Tiffany / Cartier campaign quality --ar 4:5 --s 200
```

### 129. Sustainable Fashion

```
Sustainable fashion campaign photograph of [SUBJECT: e.g., "a model in an undyed organic cotton jumpsuit with raw-edge details and recycled hardware"], [SETTING: e.g., "a ceramics studio with natural materials — clay, wood, stone"], earthy and authentic, natural light, muted earth-tone palette, the aesthetic communicates the ethics, Patagonia meets Eileen Fisher, conscious luxury --ar 2:3 --s 150
```

### 130. Vintage / Retro Fashion

```
Retro-styled fashion photograph of [SUBJECT: e.g., "a model in a 1960s-inspired A-line mini dress with bold geometric print, go-go boots, and a beehive updo"], [SETTING: e.g., "a mid-century modern interior with Eames furniture"], color-saturated, shot to emulate period film stock, slightly warm color cast, vintage fashion editorial, Twiggy-era energy, playful and iconic --ar 2:3 --s 300
```

---

## Category 8: Food Photography (20 Prompts)

### 131. Overhead Flat Lay — Full Spread

```
Overhead flat lay food photography of [SPREAD: e.g., "a complete Italian antipasto spread — cured meats, olives, artisan cheeses, roasted peppers, focaccia, grissini, olive oil, and fig jam"], arranged on [SURFACE: e.g., "a large marble board and dark linen tablecloth"], hands reaching in from opposite sides, communal and abundant, warm natural top light, editorial food styling, Bon Appetit magazine quality --ar 1:1 --s 150
```

### 132. 45-Degree Hero Shot

```
Hero food photograph at 45-degree angle of [DISH: e.g., "a bowl of ramen — rich tonkotsu broth, perfectly halved soft-boiled egg, chashu pork, nori, scallions, sesame seeds, and steam rising"], [SURFACE: e.g., "dark ceramic bowl on black slate"], key light from camera left creating depth, shallow depth of field focused on the egg, chopsticks resting on the rim, moody and atmospheric, Japanese izakaya aesthetic --ar 4:5 --s 200
```

### 133. Ingredient Close-Up

```
Close-up ingredient photography of [INGREDIENT: e.g., "a split vanilla bean with tiny seeds visible, lying across a pile of raw cane sugar, with a small glass bottle of vanilla extract nearby"], macro-level detail, individual seeds and sugar crystals visible, warm directional side light, shallow depth of field, [SURFACE: e.g., "rustic parchment paper on weathered wood"], ingredient story, cookbook photography quality --ar 3:2 --s 150
```

### 134. Pouring / Drizzling Action

```
Action food photograph of [ACTION: e.g., "thick, glossy chocolate ganache being poured over a layer cake, flowing down the sides in slow, viscous streams"], frozen motion with perfect flow visible, dark background to make the chocolate pop, studio lighting with backlight catching the sheen of the ganache, decadent and indulgent, pastry chef's showpiece, commercial bakery advertising --ar 4:5 --s 200
```

### 135. Cocktail / Beverage — Craft

```
Craft cocktail photography of [DRINK: e.g., "a smoky mezcal margarita in a coupe glass, with a charred rosemary sprig still trailing smoke, black salt rim, dehydrated lime wheel"], [SETTING: e.g., "dark moody bar, backlit bottles in soft bokeh"], drink lit from behind to glow, smoke frozen in the air, condensation on the glass, sophisticated and atmospheric, craft cocktail bar marketing --ar 4:5 --s 200
```

### 136. Bakery / Pastry

```
Bakery photography of [ITEM: e.g., "a dozen croissants fresh from the oven, golden-brown and flaky, arranged in a rustic basket lined with linen, one broken open revealing buttery layers"], warm morning light, steam or warmth haze visible, [SETTING: e.g., "a French bakery counter with flour dusting and a copper pot of jam"], golden warm tones, artisanal and authentic, boulangerie aesthetic --ar 3:2 --s 200
```

### 137. Dessert — Close-Up

```
Dessert close-up photography of [DESSERT: e.g., "a slice of tiramisu showing distinct layers — ladyfinger, mascarpone cream, cocoa dusting — on a white plate with a fork having taken one bite"], [ANGLE: e.g., "straight-on side view showing the layers"], shallow depth of field on the exposed layers, warm ambient light, cocoa powder scattered on the plate, elegant and indulgent, pastry magazine quality --ar 4:5 --s 150
```

### 138. Farm-to-Table / Rustic

```
Rustic farm-to-table food photography of [DISH: e.g., "a whole roasted chicken with root vegetables in a cast iron skillet, fresh herbs scattered, served with crusty bread on a wooden cutting board"], [SETTING: e.g., "farmhouse kitchen table, checked cloth napkin, wildflowers in a mason jar"], warm directional window light, comfort food aesthetic, rustic but intentional, Ina Garten / Barefoot Contessa styling --ar 3:2 --s 150
```

### 139. Coffee / Latte Art

```
Coffee photography of [COFFEE: e.g., "a latte with detailed rosetta latte art, in a wide ceramic cup on a saucer"], overhead angle showing the art clearly, [SURFACE: e.g., "light wood cafe table with a small pastry and a newspaper edge visible"], warm morning light from the side, shallow depth of field, steam visible above the cup, cozy and inviting, specialty coffee shop marketing --ar 1:1 --s 100
```

### 140. Pizza — Cheese Pull

```
Dynamic pizza photography of [PIZZA: e.g., "a Neapolitan margherita pizza with one slice being lifted, stretching mozzarella in a dramatic cheese pull"], warm and golden, charred leopard-spotted crust, fresh basil, bright red San Marzano sauce visible, shot from slightly above, [SETTING: e.g., "a pizza stone on a restaurant table"], the cheese pull is the hero moment, pizzeria marketing quality --ar 4:5 --s 150
```

### 141. Ice Cream / Frozen

```
Ice cream photography of [SUBJECT: e.g., "three scoops of artisanal gelato — pistachio, stracciatella, and blood orange — in a waffle cone"], [ACTION: e.g., "a drip of pistachio just beginning to run down the cone"], bright and playful, clean pastel background, studio lighting, slightly melting for texture and appeal, summer and indulgent, artisanal gelato shop branding --ar 4:5 --s 150
```

### 142. Sushi / Japanese

```
Japanese food photography of [DISH: e.g., "an omakase sushi platter — 8 pieces of nigiri on a minimalist black slate board, gari, wasabi, and soy sauce in small ceramic dishes"], [STYLE: e.g., "clean and precise, each piece perfectly placed with intentional spacing"], natural light, minimalist composition, negative space, precision and artistry, Michelin-star Japanese restaurant quality --ar 16:9 --s 100
```

### 143. Smoothie Bowl — Colorful

```
Colorful smoothie bowl photography of [BOWL: e.g., "a bright purple acai bowl topped with sliced banana, fresh berries, granola, coconut flakes, chia seeds, and a drizzle of honey"], overhead angle, arranged in visually striking pattern, [SURFACE: e.g., "white marble with tropical leaves as props"], vibrant and healthy, bright natural light, Instagram-perfect, wellness lifestyle brand quality --ar 1:1 --s 100
```

### 144. Steak — Fine Dining

```
Fine dining food photography of [DISH: e.g., "a 12oz ribeye, reverse-seared with a perfect medium-rare center, sliced and fanned on a white plate with herb compound butter melting on top, charred broccolini, and a red wine reduction"], plated with fine-dining precision, [LIGHTING: e.g., "dramatic side light creating depth in the char marks"], smoke or steam from the hot surface, carnivorous and luxurious, steakhouse marketing --ar 4:5 --s 200
```

### 145. Tacos — Styled

```
Styled taco photography of [TACOS: e.g., "three al pastor tacos on corn tortillas with pineapple, cilantro, onion, and lime wedges, held in a taco holder"], [SETTING: e.g., "colorful Mexican tile surface with salsa verde in a molcajete and a cold beer"], vibrant colors, warm light, casual and festive, authentic street food aesthetic, Mexican restaurant marketing quality --ar 3:2 --s 150
```

### 146. Charcuterie Board

```
Charcuterie board photography of [BOARD: e.g., "an elaborate grazing board with imported cheeses, prosciutto, salami, grapes, figs, nuts, honeycomb, olives, and artisan crackers"], [SURFACE: e.g., "large olive wood board on a linen-covered table"], overhead angle, abundant and overflowing, warm golden hour light, each element carefully placed yet looking naturally bountiful, entertaining and hosting aesthetic --ar 1:1 --s 150
```

### 147. Soup — Winter Comfort

```
Winter comfort food photography of [SOUP: e.g., "a bowl of creamy butternut squash soup with a swirl of cream, toasted pumpkin seeds, and a crack of black pepper"], [SETTING: e.g., "dark ceramic bowl on a wooden tray with crusty bread torn open"], warm directional side light, steam rising visibly, cozy and nourishing, autumn/winter color palette — warm oranges, dark wood, cream, hygge food photography --ar 4:5 --s 150
```

### 148. Breakfast — Morning Light

```
Breakfast photography of [MEAL: e.g., "sunny-side-up eggs with runny yolks, crispy bacon, sourdough toast with butter, and a glass of fresh orange juice"], [SETTING: e.g., "a kitchen table next to a window, morning sunlight streaming in, newspaper and coffee cup in background"], warm golden morning light, appetizing and inviting, the yolk about to break, lazy weekend morning mood, brunch restaurant marketing --ar 3:2 --s 150
```

### 149. Chocolate / Confection

```
Chocolate photography of [SUBJECT: e.g., "artisan chocolate truffles — 6 varieties in a minimalist box, each with different toppings and finishes: dusted cocoa, sea salt flakes, gold leaf, pistachio crumb, dried raspberry, and caramel drizzle"], [STYLE: e.g., "dramatic studio lighting, each truffle catching light differently on its textured surface"], dark background, luxurious and gift-worthy, chocolatier marketing, rich and indulgent --ar 4:5 --s 200
```

### 150. Recipe Process — Step by Step

```
Step-by-step recipe process photography of [RECIPE: e.g., "making fresh pasta from scratch"], 4-6 frames showing key stages — [STEPS: e.g., "flour well with eggs, kneading dough, rolling through pasta machine, cutting fettuccine, finished dish plated"], consistent lighting and surface across all frames, hands visible for human element, warm kitchen environment, cookbook photography quality, each step clear and beautiful --ar 3:2 --s 100
```

---

## Bonus: Prompt Modification Templates

### A. Change the Mood
Take any prompt above and append one of these mood modifiers:

- `serene and peaceful, soft pastel tones`
- `dramatic and intense, high contrast, deep shadows`
- `warm and nostalgic, vintage film tones, golden light`
- `cold and clinical, desaturated, sharp and precise`
- `dreamy and ethereal, soft focus, light leaks`
- `dark and moody, low key, atmospheric`
- `vibrant and energetic, saturated colors, dynamic`

### B. Change the Season
- `spring — cherry blossoms, fresh green, soft pink, morning dew`
- `summer — golden light, vivid greens, blue sky, warm tones`
- `autumn — red and gold leaves, warm amber light, misty mornings`
- `winter — snow-covered, cool blue tones, warm interior glow, frost`

### C. Add Human Element
- `a person in the distance for scale`
- `hands interacting with the subject`
- `candid moment of discovery or wonder`
- `viewed over someone's shoulder`

---

**End of Prompt Pack — 150+ Prompts**

Questions about specific prompts or need a custom combination? The frameworks above can be mixed and matched to create thousands of unique prompt variations.
