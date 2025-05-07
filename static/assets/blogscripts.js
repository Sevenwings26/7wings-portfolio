
// Screen Screen
const menuToggle = document.getElementById('menu-toggle');
const navMenu = document.getElementById('nav-menu');
const menuCancel = document.getElementById('menu-cancel');

menuToggle.addEventListener('click', () => {
    navMenu.classList.add('active');
});

menuCancel.addEventListener('click', () => {
    navMenu.classList.remove('active');
});

