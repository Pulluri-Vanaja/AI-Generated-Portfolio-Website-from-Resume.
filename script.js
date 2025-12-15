// Optional: Add any JavaScript functionality here if needed.
// For example, smooth scrolling, animations, or interactive elements.

document.addEventListener('DOMContentLoaded', () => {
    // Example: Add a subtle fade-in animation to sections on scroll
    const sections = document.querySelectorAll('main section');

    const observer = new IntersectionObserver((entries, observer) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.style.opacity = '1';
                entry.target.style.transform = 'translateY(0)';
                observer.unobserve(entry.target);
            }
        });
    }, {
        threshold: 0.1, // Trigger when 10% of the section is visible
        rootMargin: "0px 0px -50px 0px" // Start observing slightly before it enters viewport
    });

    sections.forEach(section => {
        section.style.opacity = '0';
        section.style.transform = 'translateY(20px)';
        section.style.transition = 'opacity 0.6s ease-out, transform 0.6s ease-out';
        observer.observe(section);
    });
});