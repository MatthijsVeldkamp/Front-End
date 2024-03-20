const copyright = document.getElementById('copyright');
const year = new Date().getFullYear();
const minecraft = document.getElementById('minecraft');
const boneworks = document.getElementById('boneworks');
const portal2 = document.getElementById('portal2');
const back = document.getElementById('back');
const gamepicker = document.getElementById('gamepicker');
copyright.textContent = `©${year}`;

minecraft.addEventListener('click', () => {
    location.href = 'minecraft.html';
});

boneworks.addEventListener('click', () => {
    location.href = 'boneworks.html';
});

portal2.addEventListener('click', () => {
    location.href = 'portal2.html';
});

back.addEventListener('click', () => {
    location.href = 'index.html';
});

gamepicker.addEventListener('click', () => {
    location.href = 'gamepicker.html';
});