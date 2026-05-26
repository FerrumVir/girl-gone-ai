const fs = require('fs');
const path = require('path');

const FEEDBACK_FILE = path.join('/tmp', 'girlgone-task-feedback.json');

// Script bank — keyed by product name pattern
const SCRIPT_BANK = [
  { match: /side.hustle|launch.kit/i, scripts: [
    "You keep saying you want a side hustle but you have no idea where to start. This kit has everything. Business model templates, pricing guides, launch checklists. Comment HUSTLE.",
    "I spent three months planning my first side hustle. You can do it in one weekend with this kit. Templates, checklists, the whole playbook. Link in bio.",
  ], hashtags: '#sidehustle #entrepreneur #businesstools #girlgoneai #passiveincome #onlinebusiness' },
  { match: /resume/i, scripts: [
    "Your resume is getting ignored and I know why. It looks like everyone else's. This kit has templates that actually stand out plus the exact words recruiters search for. Comment RESUME.",
    "Stop sending the same boring resume to fifty jobs. This builder kit gives you templates that recruiters actually notice. Link in bio.",
  ], hashtags: '#resume #jobsearch #careeradvice #girlgoneai #jobhunting #resumetips' },
  { match: /interview/i, scripts: [
    "Your next interview could change your life. Don't wing it. This system has answer frameworks, confidence scripts, and follow-up templates. Comment INTERVIEW.",
    "I bombed three interviews before I built this system. Answer templates, body language tips, salary negotiation scripts. You'll thank me later.",
  ], hashtags: '#interview #jobinterview #careeradvice #girlgoneai #interviewtips #dreamjob' },
  { match: /salary|negotiat/i, scripts: [
    "You left money on the table at your last job offer. This playbook has the exact scripts and frameworks to negotiate like a pro. Comment SALARY.",
    "Most people accept the first offer. Don't be most people. This playbook has word-for-word scripts to negotiate your salary. Link in bio.",
  ], hashtags: '#salarynegotiation #career #moneytips #girlgoneai #knowyourworth #payraise' },
  { match: /study.planner|study.system/i, scripts: [
    "Studying without a system is just staring at a textbook and hoping for the best. This planner has spaced repetition, focus blocks, and exam countdowns built in. Comment STUDY.",
    "I went from C's to A's when I stopped studying harder and started studying smarter. This planner has the exact system. Link in bio.",
  ], hashtags: '#studytips #student #studyplanner #girlgoneai #college #productivity' },
  { match: /language/i, scripts: [
    "You downloaded Duolingo six months ago and gave up after two weeks. This tracker actually keeps you going with streak tracking, vocab logs, and weekly goals. Comment LANGUAGE.",
  ], hashtags: '#languagelearning #polyglot #studytips #girlgoneai #learnlanguages' },
  { match: /thesis|research.writ/i, scripts: [
    "Writing a thesis feels impossible until you break it down. This planner turns your giant scary paper into daily manageable tasks. Literature review tracker, citation manager, deadline system. Comment THESIS.",
  ], hashtags: '#thesis #gradschool #research #academicwriting #girlgoneai #phdlife' },
  { match: /career.pivot/i, scripts: [
    "You hate your job but changing careers feels too risky. This roadmap breaks it into steps so small they don't feel scary. Skills gap analysis, timeline, action plan. Comment PIVOT.",
    "I changed careers at twenty-eight and everyone thought I was crazy. This roadmap is the system I wish I had. Link in bio.",
  ], hashtags: '#careerpivot #careerchange #newcareer #girlgoneai #quitYourJob #motivation' },
  { match: /course.notes/i, scripts: [
    "You've bought twelve online courses and finished zero. This notes system helps you actually retain what you learn with structured templates and action items. Comment COURSES.",
  ], hashtags: '#onlinecourses #learning #productivity #girlgoneai #selfdevelopment' },
  { match: /certification|exam.track/i, scripts: [
    "Studying for a certification without a tracker is like driving without GPS. This system maps your study plan, tracks practice scores, and counts down to exam day. Comment CERT.",
  ], hashtags: '#certification #examprep #studyplan #girlgoneai #career #professionaldevelopment' },
  { match: /network.*crm/i, scripts: [
    "You meet amazing people and then forget to follow up. This CRM tracks every connection, reminds you to reach out, and builds your network on autopilot. Comment NETWORK.",
  ], hashtags: '#networking #crm #careertools #girlgoneai #businessrelationships #linkedintips' },
  { match: /home.organiz/i, scripts: [
    "Your house is a mess and you keep buying storage bins that don't help. This system gives you room-by-room checklists, declutter workflows, and maintenance schedules. Comment HOME.",
  ], hashtags: '#homeorganization #declutter #cleaningtips #girlgoneai #organizedhome #homelife' },
  { match: /client.crm|pipeline/i, scripts: [
    "If you're tracking clients in your Notes app, we need to talk. This CRM has full pipeline tracking, follow-up reminders, and revenue dashboards. Comment CRM.",
  ], hashtags: '#crm #freelance #clientmanagement #girlgoneai #businesstools #solopreneur' },
  { match: /podcast/i, scripts: [
    "You want to start a podcast but you're stuck on equipment lists and editing software. This kit has everything from episode templates to guest outreach scripts. Comment PODCAST.",
    "Starting a podcast is easier than you think when you have the right system. Equipment guide, episode planner, launch checklist. Link in bio.",
  ], hashtags: '#podcast #podcasting #podcastlaunch #girlgoneai #contentcreator #audiocontent' },
  { match: /adhd/i, scripts: [
    "My ADHD brain needed a planner that doesn't make me feel like a failure. This one actually works with how your brain thinks. Comment FOCUS.",
    "ADHD planning isn't about doing more. It's about doing the right things at the right time. This planner gets it. Link in bio.",
  ], hashtags: '#adhd #adhdtiktok #adhdplanner #productivity #focushacks #girlgoneai #neurodivergent' },
  { match: /budget|expense/i, scripts: [
    "You make decent money and still have no idea where it goes. This tracker breaks it down so you actually see the leaks. Comment BUDGET.",
  ], hashtags: '#budgeting #personalfinance #moneytips #girlgoneai #savemoney #financialfreedom' },
  { match: /habit/i, scripts: [
    "You've tried building habits before and quit after a week. This tracker uses streaks and visual progress to keep you going. Comment HABITS.",
  ], hashtags: '#habits #habittracker #selfimprovement #girlgoneai #dailyroutine #productivity' },
  { match: /content.creator|content.calendar/i, scripts: [
    "Posting randomly and hoping for engagement isn't a strategy. This calendar plans your content weeks ahead with templates for every platform. Comment CONTENT.",
  ], hashtags: '#contentcreator #socialmedia #contentcalendar #girlgoneai #creatoreconomy #marketing' },
  { match: /wedding/i, scripts: [
    "Planning a wedding without the chaos. Every detail organized in one dashboard. Comment WEDDING.",
    "Your wedding binder is a mess and Pinterest isn't a plan. This dashboard tracks vendors, budget, timeline, everything. Link in bio.",
  ], hashtags: '#weddingplanning #bridetobe #engaged #weddingdashboard #girlgoneai #weddingorganization' },
  { match: /meal.prep|recipe/i, scripts: [
    "You spend thirty minutes every night staring at the fridge asking what's for dinner. This planner solves it for the whole week in one session. Comment MEALPREP.",
  ], hashtags: '#mealprep #mealplanning #healthyeating #girlgoneai #recipes #foodprep' },
  { match: /job.search/i, scripts: [
    "Applying to jobs without a system is why you're burned out and getting ghosted. This command center tracks every application, follow-up, and interview in one place. Comment JOBSEARCH.",
  ], hashtags: '#jobsearch #jobhunting #careeradvice #girlgoneai #hiringseason #getthejob' },
  { match: /invoice|freelance/i, scripts: [
    "If you're sending invoices from a Google Doc template you found in 2019, it's time to upgrade. Professional templates, payment tracking, client management. Comment INVOICE.",
  ], hashtags: '#freelance #invoicing #freelancetips #girlgoneai #solopreneur #getpaid' },
  { match: /wellness|habit.track/i, scripts: [
    "Self-care isn't just face masks. This tracker covers sleep, hydration, exercise, mood, and habits in one beautiful system. Comment WELLNESS.",
  ], hashtags: '#wellness #selfcare #healthyhabits #girlgoneai #wellnesstracker #mentalhealth' },
  { match: /amazon.fba|product.research/i, scripts: [
    "Starting on Amazon? Research templates for niche selection, BSR analysis, supplier vetting, PPC planning. Everything before your first order. Comment FBA.",
  ], hashtags: '#amazonfba #amazonbusiness #ecommerce #sidehustle #entrepreneur #girlgoneai' },
  { match: /digital.product.launch|launch.playbook/i, scripts: [
    "Your digital product idea is worth nothing until you launch it. This blueprint covers validation, pricing, landing pages, and launch sequence. Comment LAUNCH.",
  ], hashtags: '#digitalproducts #productlaunch #entrepreneur #onlinebusiness #girlgoneai #creatoreconomy' },
  { match: /photography|photo.*client/i, scripts: [
    "If you're still managing photography clients in your Notes app, you're losing bookings. Pipeline, checklists, contracts, communication — one system. Comment PHOTO.",
  ], hashtags: '#photographer #photographybusiness #clientmanagement #girlgoneai #bookmoreclients' },
  { match: /vacation.rental|airbnb/i, scripts: [
    "Managing your Airbnb from your Notes app is costing you bookings. Property portfolio, guest communication, pricing strategy, cleaning checklists. Comment RENTAL.",
  ], hashtags: '#airbnb #airbnbhost #vacationrental #propertymanagement #girlgoneai #passiveincome' },
  { match: /proposal|client.proposal/i, scripts: [
    "Your proposals look like they were made in five minutes because they were. These templates make you look professional without the hours of formatting. Comment PROPOSAL.",
  ], hashtags: '#freelance #proposals #clientwork #girlgoneai #businesstools #solopreneur' },
  { match: /coding|developer|prompt.pack/i, scripts: [
    "Stop copying prompts from random Twitter threads. This pack has tested, organized prompts for every coding workflow. Comment CODE.",
  ], hashtags: '#coding #developer #aiprompts #girlgoneai #programming #devtools' },
  { match: /midjourney|ai.art/i, scripts: [
    "Your Midjourney prompts are giving generic. This pack has structured prompts that actually produce the aesthetic you want. Comment ART.",
  ], hashtags: '#midjourney #aiart #aiprompts #girlgoneai #digitalart #creativetools' },
  { match: /teacher|lesson.plan/i, scripts: [
    "Teachers, stop spending your Sunday nights buried in lesson plans. This planner organizes everything in one place. Lesson plans, seating charts, grade tracking. And it's completely free. Comment TEACHER.",
  ], hashtags: '#teacher #teacherlife #lessonplanning #girlgoneai #education #teachersoftiktok' },
];

const GENERIC_SCRIPTS = [
  (name, price) => `${name}. ${price === 'FREE' ? 'Completely free.' : price + '.'} Built to actually help, not just look pretty. Link in bio.`,
  (name, price) => `Stop overthinking it. ${name} has everything you need in one place. ${price === 'FREE' ? 'And it costs nothing.' : price + '. Link in bio.'}`,
  (name, price) => `This is the tool I wish I had when I started. ${name}. ${price === 'FREE' ? 'Free.' : price + '.'} Comment INFO for details.`,
];

function seededRandom(seed) {
  let h = 0;
  for (let i = 0; i < seed.length; i++) {
    h = ((h << 5) - h + seed.charCodeAt(i)) | 0;
  }
  return function() {
    h = (h * 16807 + 0) % 2147483647;
    return (h & 0x7fffffff) / 2147483647;
  };
}

function loadFeedback() {
  try {
    return JSON.parse(fs.readFileSync(FEEDBACK_FILE, 'utf8'));
  } catch {
    return { actions: [], productScores: {} };
  }
}

function getScriptForProduct(product, rng) {
  const title = (product.title || '').replace(/&amp;/g, '&').replace(/&lt;/g, '<').replace(/&gt;/g, '>');
  const price = product.price > 0 ? `$${product.price}` : 'FREE';

  for (const entry of SCRIPT_BANK) {
    if (entry.match.test(title)) {
      const script = entry.scripts[Math.floor(rng() * entry.scripts.length)];
      return { script, hashtags: entry.hashtags, price };
    }
  }

  const gen = GENERIC_SCRIPTS[Math.floor(rng() * GENERIC_SCRIPTS.length)];
  return {
    script: gen(title, price),
    hashtags: '#digitalproducts #girlgoneai #templates #productivity #onlinebusiness',
    price,
  };
}

module.exports = async function handler(req, res) {
  const today = new Date().toISOString().slice(0, 10);
  const rng = seededRandom(today + '-girlgoneai-daily');

  // Load catalog
  let catalog = [];
  try {
    const raw = fs.readFileSync(path.join(__dirname, '..', 'products', 'catalog.json'), 'utf8');
    catalog = JSON.parse(raw);
  } catch (e) {
    return res.status(500).json({ error: 'Catalog not found' });
  }

  // Load feedback scores
  const fb = loadFeedback();
  const scores = fb.productScores || {};

  // Recent actions — find slugs shown in last 3 days to avoid repeats
  const recentDays = new Set();
  const threeDaysAgo = new Date(Date.now() - 3 * 86400000).toISOString().slice(0, 10);
  const recentSlugs = new Set();
  for (const a of (fb.actions || [])) {
    if (a.timestamp && a.timestamp.slice(0, 10) >= threeDaysAgo && a.slug) {
      recentSlugs.add(a.slug);
    }
  }

  // Filter to sellable products
  const sellable = catalog.filter(p => p.price > 0 && !p.slug.includes('bundle'));

  // Score each product for selection weight
  const weighted = sellable.map(p => {
    let weight = 10; // base weight

    // Feedback score: products Jaci completes get boosted, ignored get suppressed
    const ps = scores[p.slug] || scores[p.title] || null;
    if (ps) {
      weight += ps.score; // done=+2, replied=+1, ignored=-2 cumulative
      // Hard suppress: if ignored 3+ times with no completions, weight drops to 1
      if (ps.ignored >= 3 && ps.done === 0) weight = 1;
      // Boost: if done 2+ times, it's a winner — always keep in rotation
      if (ps.done >= 2) weight = Math.max(weight, 15);
    }

    // Recency penalty: shown in last 3 days → reduce weight (variety)
    if (recentSlugs.has(p.slug)) weight = Math.max(1, Math.floor(weight / 3));

    // Higher-priced products get slight boost (more revenue per post)
    if (p.price >= 15) weight += 2;
    if (p.price >= 19) weight += 1;

    // Floor at 1 — never fully exclude
    weight = Math.max(1, weight);

    return { product: p, weight };
  });

  // Weighted random selection: pick 5 products
  const picked = [];
  const pool = weighted.slice();
  for (let i = 0; i < 5 && pool.length > 0; i++) {
    const totalWeight = pool.reduce((s, p) => s + p.weight, 0);
    let r = rng() * totalWeight;
    let idx = 0;
    for (let j = 0; j < pool.length; j++) {
      r -= pool[j].weight;
      if (r <= 0) { idx = j; break; }
    }
    picked.push(pool[idx].product);
    pool.splice(idx, 1);
  }

  const tasks = picked.map((product, i) => {
    const title = (product.title || '').replace(/&amp;/g, '&').replace(/&lt;/g, '<').replace(/&gt;/g, '>');
    const { script, hashtags, price } = getScriptForProduct(product, rng);
    const gumroadLink = `https://girlgoneai.gumroad.com/l/${product.slug}`;
    const siteLink = `https://girlgone.ai/products/${product.slug}.html`;

    return {
      id: `daily_${today}_${i + 1}`,
      title: `${title} — Social Push`,
      product: title,
      slug: product.slug,
      price,
      script,
      hashtags,
      productLink: gumroadLink,
      siteLink,
      desc: `Format: TikTok + Instagram Reel\nPost with caption, hashtags, and product link.`,
      status: 'pending',
    };
  });

  // Evening showcase
  const names = tasks.slice(0, 4).map(t => t.product.split(' ').slice(0, 3).join(' ')).join(', ');
  tasks.push({
    id: `daily_${today}_showcase`,
    title: 'Evening Showcase — All Products',
    product: 'Full Catalog Push',
    slug: '',
    price: '$6-$19',
    script: `${tasks.length} products featured today. ${names}. All digital, all instant download, all under twenty dollars. Link in bio.`,
    hashtags: '#digitalproducts #entrepreneur #sidehustle #girlgoneai #businesstools #makemoneyonline',
    productLink: 'https://girlgoneai.gumroad.com',
    siteLink: 'https://girlgone.ai',
    desc: 'Format: TikTok + IG Story (evening)\nShowcase all featured products. Cross-sell angle.',
    status: 'pending',
  });

  // Include feedback summary so dashboard can show Jaci her impact
  const totalDone = (fb.actions || []).filter(a => a.action === 'done').length;
  const totalIgnored = (fb.actions || []).filter(a => a.action === 'ignored').length;
  const totalReplied = (fb.actions || []).filter(a => a.action === 'replied').length;

  res.setHeader('Cache-Control', 'public, max-age=300');
  return res.status(200).json({
    date: today,
    tasks,
    stats: {
      totalDone,
      totalReplied,
      totalIgnored,
      productsTracked: Object.keys(scores).length,
    },
  });
};
