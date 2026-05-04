// Header scroll effect
const header = document.getElementById('header');
window.addEventListener('scroll', () => {
  header.classList.toggle('scrolled', window.scrollY > 20);
}, { passive: true });

// Mobile menu toggle
const menuBtn = document.getElementById('menuBtn');
const nav = document.getElementById('nav');
menuBtn.addEventListener('click', () => {
  menuBtn.classList.toggle('active');
  nav.classList.toggle('active');
});

// Close mobile menu on nav link click
nav.querySelectorAll('a').forEach(link => {
  link.addEventListener('click', () => {
    nav.classList.remove('active');
    menuBtn.classList.remove('active');
  });
});

// Smooth scroll for anchor links
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
  anchor.addEventListener('click', (e) => {
    const target = document.querySelector(anchor.getAttribute('href'));
    if (target) {
      e.preventDefault();
      const offset = header.offsetHeight + 16;
      const top = target.getBoundingClientRect().top + window.scrollY - offset;
      window.scrollTo({ top, behavior: 'smooth' });
    }
  });
});

// Newsletter form submission
const form = document.getElementById('newsletter-form');
if (form) {
  form.addEventListener('submit', async (e) => {
    e.preventDefault();
    const emailInput = form.querySelector('input[type="email"]');
    if (emailInput && emailInput.value) {
      const btn = form.querySelector('button');
      if (btn) btn.disabled = true;
      try {
        await fetch('/api/subscribe', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({ email: emailInput.value, source: 'newsletter' }),
        });
      } catch (err) {
        // Still show success — form capture is best-effort
      }
      form.innerHTML = '<p style="color: var(--pink); font-weight: 600; font-size: 1.1rem; padding: 16px 0;">You\'re in! Welcome to the Girl Gone AI community.</p>';
    }
  });
}

// Free download modal
const freeModal = document.getElementById('free-download-modal');
const modalClose = document.getElementById('modal-close');
const freeForm = document.getElementById('free-download-form');

document.querySelectorAll('.free-download-btn').forEach(btn => {
  btn.addEventListener('click', () => {
    if (freeModal) freeModal.style.display = 'flex';
  });
});

if (modalClose) {
  modalClose.addEventListener('click', () => {
    if (freeModal) freeModal.style.display = 'none';
  });
}

if (freeModal) {
  freeModal.addEventListener('click', (e) => {
    if (e.target === freeModal) freeModal.style.display = 'none';
  });
}

if (freeForm) {
  freeForm.addEventListener('submit', async (e) => {
    e.preventDefault();
    const slug = freeForm.dataset.slug;
    const emailInput = freeForm.querySelector('input[type="email"]');
    const nameInput = freeForm.querySelector('input[name="name"]');
    const msgEl = document.getElementById('modal-msg');
    const btn = freeForm.querySelector('button');

    if (!emailInput || !emailInput.value) return;
    if (btn) btn.disabled = true;

    // Direct download path (works on static hosting without API)
    const basePath = window.location.pathname.includes('/products/') ? '..' : '.';
    const downloadUrl = basePath + '/downloads/' + encodeURIComponent(slug) + '.md';

    try {
      const resp = await fetch('/api/free-download', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          email: emailInput.value,
          name: nameInput ? nameInput.value : '',
          slug: slug,
        }),
      });
      const data = await resp.json();
      if (data.downloadUrl) {
        if (msgEl) msgEl.textContent = 'Download starting...';
        window.location.href = data.downloadUrl;
        setTimeout(() => { if (freeModal) freeModal.style.display = 'none'; }, 1500);
        return;
      }
    } catch (err) {
      // API unavailable (static hosting) — fall through to direct download
    }

    if (msgEl) msgEl.textContent = 'Download starting...';
    window.location.href = downloadUrl;
    setTimeout(() => { if (freeModal) freeModal.style.display = 'none'; }, 1500);
  });
}

// Waitlist forms (product pages)
document.querySelectorAll('.waitlist-form').forEach(wf => {
  wf.addEventListener('submit', async (e) => {
    e.preventDefault();
    const emailInput = wf.querySelector('input[type="email"]');
    const msgEl = wf.parentElement.querySelector('.waitlist-msg');
    const btn = wf.querySelector('button');
    if (!emailInput || !emailInput.value) return;
    if (btn) btn.disabled = true;
    try {
      await fetch('/api/subscribe', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          email: emailInput.value,
          source: wf.dataset.source || 'product-page',
          productSlug: wf.dataset.productSlug || '',
        }),
      });
    } catch (err) {
      // best-effort
    }
    if (msgEl) {
      msgEl.textContent = "You're on the list! We'll notify you at launch.";
      msgEl.style.color = 'var(--pink)';
    }
    wf.style.display = 'none';
  });
});

// Launching Soon popup (for products not yet available on Gumroad)
(function() {
  // Demo mode: skip all interception, let every link pass through to Gumroad
  var cfg = window.NOVOCLAW_CONFIG || {};
  if (cfg.demoMode) return;

  // Known working Gumroad slugs — all others get the Launching Soon popup
  var liveGumroadSlugs = [
    'apbls','baqfdx','btxunu','free-starter-kit','gkdlq','hxntlz',
    'rjfayx','rypqg','thtyoc','wgnvf','xrlbjs','27-podcast-launch-kit'
  ];

  // Select explicit fallback buttons + Gumroad links with non-live slugs
  var fallbackBtns = document.querySelectorAll('.fallback-buy-btn');
  var gumroadBtns = document.querySelectorAll('a.buy-btn[href*="gumroad.com/l/"], a.gumroad-buy-btn[href*="gumroad.com/l/"], .gumroad-link[href*="gumroad.com/l/"]');
  var intercepted = [];

  fallbackBtns.forEach(function(btn) { intercepted.push(btn); });
  gumroadBtns.forEach(function(btn) {
    var href = btn.getAttribute('href') || '';
    var m = href.match(/\/l\/([^/?#]+)/);
    if (m && liveGumroadSlugs.indexOf(m[1]) === -1) {
      intercepted.push(btn);
    }
  });

  if (!intercepted.length) return;

  // Create modal overlay
  var overlay = document.createElement('div');
  overlay.className = 'launching-soon-overlay';
  overlay.innerHTML =
    '<div class="launching-soon-modal">' +
      '<button class="modal-close-btn" aria-label="Close">&times;</button>' +
      '<h2>Launching Soon</h2>' +
      '<p>This product is launching soon! Leave your email and a message below, and Jaci will happily move it to the next release for you.</p>' +
      '<form id="launching-soon-form">' +
        '<input type="email" name="email" placeholder="Your email..." required>' +
        '<textarea name="message" placeholder="Your message (optional)..." rows="3"></textarea>' +
        '<input type="hidden" name="product" value="">' +
        '<button type="submit">Notify Me</button>' +
      '</form>' +
    '</div>';
  document.body.appendChild(overlay);

  var form = document.getElementById('launching-soon-form');
  var productInput = form.querySelector('input[name="product"]');

  // Replace all intercepted links with launching-soon buttons
  intercepted.forEach(function(btn) {
    btn.textContent = 'Launching Soon';
    btn.addEventListener('click', function(e) {
      e.preventDefault();
      // Extract product slug from href or parent data
      var slug = '';
      var href = btn.getAttribute('href') || '';
      var match = href.match(/\/l\/(.+)$/);
      if (match) slug = match[1];
      productInput.value = slug;
      // Reset form state
      form.reset();
      productInput.value = slug;
      var successMsg = overlay.querySelector('.modal-success');
      if (successMsg) successMsg.remove();
      form.style.display = '';
      overlay.classList.add('active');
    });
  });

  // Close modal
  overlay.querySelector('.modal-close-btn').addEventListener('click', function() {
    overlay.classList.remove('active');
  });
  overlay.addEventListener('click', function(e) {
    if (e.target === overlay) overlay.classList.remove('active');
  });

  // Form submit
  form.addEventListener('submit', function(e) {
    e.preventDefault();
    var emailInput = form.querySelector('input[type="email"]');
    var messageInput = form.querySelector('textarea');
    var submitBtn = form.querySelector('button[type="submit"]');
    if (!emailInput || !emailInput.value) return;
    submitBtn.disabled = true;

    // Post to subscribe endpoint (best-effort on static hosting)
    try {
      fetch('/api/subscribe', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          email: emailInput.value,
          message: messageInput ? messageInput.value : '',
          source: 'launching-soon',
          productSlug: productInput.value,
        }),
      }).catch(function() {});
    } catch (err) {}

    // Also submit via Formsubmit as backup for static hosting
    var cfg = window.NOVOCLAW_CONFIG || {};
    if (cfg.formsubmitEmail) {
      try {
        fetch('https://formsubmit.co/ajax/' + cfg.formsubmitEmail, {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({
            email: emailInput.value,
            message: messageInput ? messageInput.value : '',
            product: productInput.value,
            _subject: 'Launching Soon Request: ' + productInput.value,
          }),
        }).catch(function() {});
      } catch (err) {}
    }

    // Show success
    form.style.display = 'none';
    var msg = document.createElement('p');
    msg.className = 'modal-success';
    msg.textContent = "You're on the list! We'll let you know when it drops.";
    form.parentNode.appendChild(msg);
    submitBtn.disabled = false;
  });
})();

// Demo mode: hide "Coming Soon" badges, add product page links
(function() {
  var cfg = window.NOVOCLAW_CONFIG || {};
  if (!cfg.demoMode) return;

  // Hide Coming Soon badges
  document.querySelectorAll('.coming-soon-badge').forEach(function(el) {
    el.style.display = 'none';
  });

  // Hide the Launching Soon section header
  var lsHeader = document.querySelector('.launching-soon-header');
  if (lsHeader) lsHeader.style.display = 'none';

  // Replace "Coming Soon" text with View Product links
  document.querySelectorAll('.coming-soon-text').forEach(function(el) {
    var card = el.closest('.product-card');
    if (!card) return;
    var h3 = card.querySelector('h3');
    if (!h3) return;
    var link = document.createElement('a');
    link.href = 'catalog-landing.html';
    link.textContent = 'View Product';
    link.className = 'gumroad-link';
    el.replaceWith(link);
  });
})();

// Fade-in on scroll
const observerOptions = { threshold: 0.1, rootMargin: '0px 0px -40px 0px' };
const observer = new IntersectionObserver((entries) => {
  entries.forEach(entry => {
    if (entry.isIntersecting) {
      entry.target.style.opacity = '1';
      entry.target.style.transform = 'translateY(0)';
      observer.unobserve(entry.target);
    }
  });
}, observerOptions);

document.querySelectorAll('.category-card, .social-card, .about-grid, .newsletter-inner, .catalog .bundle-card').forEach(el => {
  el.style.opacity = '0';
  el.style.transform = 'translateY(24px)';
  el.style.transition = 'opacity 0.6s ease, transform 0.6s ease';
  observer.observe(el);
});
