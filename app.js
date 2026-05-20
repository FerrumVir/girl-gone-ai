// --- Conversion event helpers ---
function fireMeta(event, params) {
  if (typeof window.fbq === 'function') {
    try { window.fbq('track', event, params || {}); } catch (e) {}
  }
}

function fireGoogleAdsConversion(label, params) {
  if (typeof window.gtag !== 'function') return;
  var cfg = window.NOVOCLAW_CONFIG || {};
  if (!cfg.googleAdsId || !label) return;
  try {
    window.gtag('event', 'conversion', Object.assign({
      send_to: cfg.googleAdsId + '/' + label,
    }, params || {}));
  } catch (e) {}
}

function fireLead(email, source) {
  fireMeta('Lead', { content_name: source || 'newsletter' });
  var cfg = window.NOVOCLAW_CONFIG || {};
  if (cfg.googleAdsLeadLabel) {
    fireGoogleAdsConversion(cfg.googleAdsLeadLabel, { value: 0, currency: 'USD' });
  }
}

// --- Fire ViewContent on product / bundle pages (for Meta ad optimization) ---
(function() {
  var m = window.location.pathname.match(/^\/(products|bundles)\/([^/]+)\.html$/);
  if (!m) return;
  var slug = decodeURIComponent(m[2]);
  fireMeta('ViewContent', {
    content_ids: [slug],
    content_type: m[1] === 'bundles' ? 'product_group' : 'product'
  });
})();

// --- Stripe checkout ---
(function() {
  document.addEventListener('click', function(e) {
    var btn = e.target.closest('.stripe-buy-btn');
    if (!btn) return;
    e.preventDefault();
    btn.disabled = true;
    var originalText = btn.textContent;
    btn.textContent = 'Loading...';

    var slug = btn.getAttribute('data-slug');

    // Fire InitiateCheckout immediately (before redirect can race the pixel)
    fireMeta('InitiateCheckout', { content_ids: [slug], content_type: 'product' });
    var cfg = window.NOVOCLAW_CONFIG || {};
    if (cfg.googleAdsInitiateCheckoutLabel) {
      fireGoogleAdsConversion(cfg.googleAdsInitiateCheckoutLabel, { value: 0, currency: 'USD' });
    }

    fetch('/api/create-checkout-session', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ slug: slug })
    })
    .then(function(r) { return r.json(); })
    .then(function(data) {
      if (data.url) {
        window.location.href = data.url;
      } else {
        alert(data.error || 'Checkout failed. Please try again.');
        btn.disabled = false;
        btn.textContent = originalText;
      }
    })
    .catch(function() {
      alert('Checkout failed. Please try again.');
      btn.disabled = false;
      btn.textContent = originalText;
    });
  });
})();

// --- Header scroll effect ---
const header = document.getElementById('header');
if (header) {
  window.addEventListener('scroll', () => {
    header.classList.toggle('scrolled', window.scrollY > 20);
  }, { passive: true });
}

// --- Mobile menu toggle ---
const menuBtn = document.getElementById('menuBtn');
const nav = document.getElementById('nav');
if (menuBtn && nav) {
  menuBtn.addEventListener('click', () => {
    menuBtn.classList.toggle('active');
    nav.classList.toggle('active');
  });
  nav.querySelectorAll('a').forEach(link => {
    link.addEventListener('click', () => {
      nav.classList.remove('active');
      menuBtn.classList.remove('active');
    });
  });
}

// --- Smooth scroll for anchor links ---
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
  anchor.addEventListener('click', (e) => {
    const target = document.querySelector(anchor.getAttribute('href'));
    if (target) {
      e.preventDefault();
      const h = document.getElementById('header');
      const offset = h ? h.offsetHeight + 16 : 80;
      const top = target.getBoundingClientRect().top + window.scrollY - offset;
      window.scrollTo({ top, behavior: 'smooth' });
    }
  });
});

// --- Shared email-signup submission helper ---
const EMAIL_RE = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;

async function submitSignup(form, payload) {
  const btn = form.querySelector('button');
  const emailInput = form.querySelector('input[type="email"]');
  const email = emailInput ? emailInput.value.trim() : '';

  if (!EMAIL_RE.test(email)) {
    showFormMessage(form, 'Please enter a valid email address.', 'error');
    return false;
  }

  if (btn) btn.disabled = true;
  showFormMessage(form, '', null);

  let resp, data;
  try {
    resp = await fetch('/api/subscribe', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(Object.assign({ email }, payload || {}))
    });
    data = await resp.json().catch(() => ({}));
  } catch (err) {
    if (btn) btn.disabled = false;
    showFormMessage(form, 'Network error. Please try again.', 'error');
    return false;
  }

  if (!resp.ok) {
    if (btn) btn.disabled = false;
    showFormMessage(form, (data && data.error) || 'Something went wrong. Please try again.', 'error');
    return false;
  }

  fireLead(email, (payload && payload.source) || 'newsletter');
  return true;
}

function showFormMessage(form, text, kind) {
  // Look for a sibling .form-msg or create one
  let msg = form.parentElement.querySelector('.form-msg');
  if (!msg) {
    msg = document.createElement('p');
    msg.className = 'form-msg';
    msg.style.marginTop = '12px';
    msg.style.fontSize = '0.95rem';
    msg.style.fontWeight = '600';
    form.parentElement.appendChild(msg);
  }
  msg.textContent = text || '';
  msg.style.color = kind === 'error' ? '#dc2626' : '#a3346a';
}

// --- Newsletter form ---
const newsletterForm = document.getElementById('newsletter-form');
if (newsletterForm) {
  newsletterForm.addEventListener('submit', async (e) => {
    e.preventDefault();
    const ok = await submitSignup(newsletterForm, { source: 'newsletter' });
    if (ok) {
      newsletterForm.innerHTML = '<p style="color: var(--pink, #a3346a); font-weight: 600; font-size: 1.1rem; padding: 16px 0;">You\'re in! Welcome to the Girl Gone AI community.</p>';
    }
  });
}

// --- Free download buttons (no email gate — direct file serve) ---
document.querySelectorAll('.free-download-btn').forEach(btn => {
  btn.addEventListener('click', () => {
    const slug = btn.dataset.slug || '';
    const name = slug.replace(/^\d+-/, '');
    fireMeta('Lead', { content_name: 'free-download', content_ids: [slug] });
    window.location.href = '/downloads/files/' + encodeURIComponent(name) + '.html';
  });
});

// --- Waitlist forms (product pages) ---
document.querySelectorAll('.waitlist-form').forEach(wf => {
  wf.addEventListener('submit', async (e) => {
    e.preventDefault();
    const ok = await submitSignup(wf, {
      source: wf.dataset.source || 'product-page',
      productSlug: wf.dataset.productSlug || '',
    });
    if (ok) {
      const msgEl = wf.parentElement.querySelector('.waitlist-msg');
      if (msgEl) {
        msgEl.textContent = "You're on the list! We'll notify you at launch.";
        msgEl.style.color = 'var(--pink, #a3346a)';
      }
      wf.style.display = 'none';
    }
  });
});

// --- Copy link share button ---
document.querySelectorAll('.share-copy').forEach(btn => {
  btn.addEventListener('click', () => {
    const url = btn.dataset.url ? new URL(btn.dataset.url, window.location.href).href : window.location.href;
    navigator.clipboard.writeText(url).then(() => {
      btn.textContent = 'Copied!';
      setTimeout(() => { btn.textContent = 'Link'; }, 2000);
    });
  });
});

// --- Exit-intent modal ---
const exitModal = document.getElementById('exit-intent-modal');
const exitClose = document.getElementById('exit-intent-close');
const exitForm = document.getElementById('exit-intent-form');

if (exitClose && exitModal) {
  exitClose.addEventListener('click', () => { exitModal.style.display = 'none'; });
  exitModal.addEventListener('click', (e) => { if (e.target === exitModal) exitModal.style.display = 'none'; });
}
if (exitModal) {
  document.addEventListener('mouseleave', (e) => {
    if (e.clientY < 0 && !sessionStorage.getItem('exitShown')) {
      exitModal.style.display = 'flex';
      sessionStorage.setItem('exitShown', '1');
    }
  });
}
if (exitForm) {
  exitForm.addEventListener('submit', async (e) => {
    e.preventDefault();
    const ok = await submitSignup(exitForm, { source: 'exit-intent' });
    if (ok) {
      const msgEl = document.getElementById('exit-intent-msg');
      if (msgEl) { msgEl.textContent = "You're in! Welcome to the community."; msgEl.style.color = 'var(--pink, #a3346a)'; }
      exitForm.style.display = 'none';
    }
  });
}

// --- Fade-in on scroll ---
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
