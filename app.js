// Stripe checkout
(function() {
  document.addEventListener('click', function(e) {
    var btn = e.target.closest('.stripe-buy-btn');
    if (!btn) return;
    e.preventDefault();
    btn.disabled = true;
    btn.textContent = 'Loading...';

    var slug = btn.getAttribute('data-slug');
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
        btn.textContent = 'Buy Now';
      }
    })
    .catch(function() {
      alert('Checkout failed. Please try again.');
      btn.disabled = false;
      btn.textContent = 'Buy Now';
    });
  });
})();

// Header scroll effect
const header = document.getElementById('header');
if (header) {
  window.addEventListener('scroll', () => {
    header.classList.toggle('scrolled', window.scrollY > 20);
  }, { passive: true });
}

// Mobile menu toggle
const menuBtn = document.getElementById('menuBtn');
const nav = document.getElementById('nav');
if (menuBtn && nav) {
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
}

// Smooth scroll for anchor links
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
      } catch (err) {}
      form.innerHTML = '<p style="color: var(--pink); font-weight: 600; font-size: 1.1rem; padding: 16px 0;">You\'re in! Welcome to the Girl Gone AI community.</p>';
    }
  });
}

// Free download — email-gated via /api/free-download
(function() {
  var modal = document.getElementById('free-download-modal');
  var closeBtn = document.getElementById('free-download-close');
  var form = document.getElementById('free-download-form');
  var slugInput = document.getElementById('free-download-slug');
  var titleEl = document.getElementById('free-download-title');
  var msgEl = document.getElementById('free-download-msg');
  var submitBtn = document.getElementById('free-download-submit');

  if (!modal || !form) return;

  document.querySelectorAll('.free-download-card').forEach(function(card) {
    card.addEventListener('click', function() {
      var slug = card.dataset.slug || '';
      var productName = card.querySelector('h3');
      slugInput.value = slug;
      titleEl.textContent = productName ? productName.textContent : 'Get Your Free Download';
      msgEl.textContent = '';
      form.style.display = '';
      if (submitBtn) { submitBtn.disabled = false; submitBtn.textContent = 'Send Me the Download'; }
      modal.style.display = 'flex';
    });
  });

  closeBtn.addEventListener('click', function() { modal.style.display = 'none'; });
  modal.addEventListener('click', function(e) { if (e.target === modal) modal.style.display = 'none'; });

  form.addEventListener('submit', function(e) {
    e.preventDefault();
    var email = form.querySelector('input[name="email"]').value;
    var name = form.querySelector('input[name="name"]').value;
    var slug = slugInput.value;
    if (!email || !slug) return;

    if (submitBtn) { submitBtn.disabled = true; submitBtn.textContent = 'Loading...'; }
    msgEl.textContent = '';

    fetch('/api/free-download', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ email: email, name: name, slug: slug })
    })
    .then(function(r) { return r.json(); })
    .then(function(data) {
      if (data.downloadUrl) {
        msgEl.style.color = '#10B981';
        msgEl.textContent = data.message || 'Success! Redirecting to your download...';
        form.style.display = 'none';
        setTimeout(function() {
          window.location.href = data.downloadUrl;
        }, 800);
      } else {
        msgEl.style.color = '#ba1a1a';
        msgEl.textContent = data.error || 'Something went wrong. Please try again.';
        if (submitBtn) { submitBtn.disabled = false; submitBtn.textContent = 'Send Me the Download'; }
      }
    })
    .catch(function() {
      msgEl.style.color = '#ba1a1a';
      msgEl.textContent = 'Network error. Please try again.';
      if (submitBtn) { submitBtn.disabled = false; submitBtn.textContent = 'Send Me the Download'; }
    });
  });
})();

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
    } catch (err) {}
    if (msgEl) {
      msgEl.textContent = "You're on the list! We'll notify you at launch.";
      msgEl.style.color = 'var(--pink)';
    }
    wf.style.display = 'none';
  });
});

// Copy link share button
document.querySelectorAll('.share-copy').forEach(btn => {
  btn.addEventListener('click', () => {
    const url = btn.dataset.url ? new URL(btn.dataset.url, window.location.href).href : window.location.href;
    navigator.clipboard.writeText(url).then(() => {
      btn.textContent = 'Copied!';
      setTimeout(() => { btn.textContent = 'Link'; }, 2000);
    });
  });
});

// Exit-intent modal
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
    const emailInput = exitForm.querySelector('input[type="email"]');
    const msgEl = document.getElementById('exit-intent-msg');
    if (!emailInput || !emailInput.value) return;
    try {
      await fetch('/api/subscribe', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ email: emailInput.value, source: 'exit-intent' }),
      });
    } catch (err) {}
    if (msgEl) { msgEl.textContent = "You're in! Welcome to the community."; msgEl.style.color = 'var(--pink)'; }
    exitForm.style.display = 'none';
  });
}

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
