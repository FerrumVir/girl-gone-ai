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
