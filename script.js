const THEME_KEY = 'portfolio-theme';

let announcer = document.getElementById('sr-announcer');
if (!announcer) {
    announcer = document.createElement('div');
    announcer.id = 'sr-announcer';
    announcer.setAttribute('aria-live', 'polite');
    announcer.setAttribute('class', 'sr-only');
    document.head.appendChild(announcer);
}

function applyTheme(theme) {
    if (theme === 'light') {
        document.body.classList.add('light-mode');
    } else {
        document.body.classList.remove('light-mode');
    }
    const btn = document.getElementById('theme-toggle');
    const tooltip = document.getElementById('theme-tooltip');
    
    if (btn) {
        const actionText = theme === 'light' ? 'Switch to dark mode' : 'Switch to light mode';
        btn.setAttribute('aria-label', actionText);
        if (tooltip) {
            tooltip.textContent = actionText;
        }
        btn.querySelector('.icon-sun').style.display = theme === 'light' ? 'none' : 'block';
        btn.querySelector('.icon-moon').style.display = theme === 'light' ? 'block' : 'none';
        if (announcer && document.readyState === 'complete') {
            announcer.textContent = theme === 'light' ? 'Light mode enabled' : 'Dark mode enabled';
        }
    }
}

document.addEventListener('DOMContentLoaded', () => {
    const saved = localStorage.getItem(THEME_KEY) || 'dark';
    applyTheme(saved);

    const btn = document.getElementById('theme-toggle');
    if (btn) {
        btn.addEventListener('click', () => {
            const isLight = document.body.classList.contains('light-mode');
            const next = isLight ? 'dark' : 'light';
            localStorage.setItem(THEME_KEY, next);
            applyTheme(next);
        });
    }

    const observerOptions = {
        root: null,
        rootMargin: '0px',
        threshold: 0.1
    };

    const observer = new IntersectionObserver((entries, obs) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('visible');
                obs.unobserve(entry.target);
            }
        });
    }, observerOptions);

    document.querySelectorAll('.fade-in').forEach(el => {
        observer.observe(el);
    });
});
