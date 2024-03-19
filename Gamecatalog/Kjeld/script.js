document.addEventListener('DOMContentLoaded', function () {
    const hamburgerIcon = document.getElementById('hamburger-icon');
    const navMenu = document.getElementById('nav-menu');

    hamburgerIcon.addEventListener('click', function () {
        // Toggle 'open' class on hamburger icon
        hamburgerIcon.classList.toggle('open');

        // Toggle 'open' class on navigation menu
        navMenu.classList.toggle('open');
    });
});