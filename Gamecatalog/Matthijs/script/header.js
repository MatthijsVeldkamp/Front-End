const minecraft = document.getElementById('minecraft');
const boneworks = document.getElementById('boneworks');
const portal2 = document.getElementById('portal2');
const video = document.getElementById('myVideo');
minecraft.addEventListener('click', () => {
    window.location.href = 'mc.html';
});



boneworks.addEventListener('click', () => {
    removecontainers();
    const container = document.createElement('div');
    container.classList.add('container');
    container.id = 'boneworkscontainer';
    const h2 = document.createElement('h2');
    h2.textContent = 'Boneworks';
    const p = document.createElement('p');
    p.textContent = "Boneworks is een VR-spel ontwikkeld en gepubliceerd door Stress Level Zero, uitgebracht op 10 december 2019. Het spel is een first-person shooter dat volledig is gebaseerd op fysica, waarbij de speler een volledig virtuele lichaam bestuurt dat reageert op de speler's echte wereldinvoer en ook op obstructies in het spelwereld. Het spel speelt zich af in een onvoltooid gesimuleerde universum waar de speler de rol van Arthur Ford, een rogue cybersecurity directeur, op zich neemt. Het spel wordt geprezen om zijn innovatieve mechanieken, boeiende verhaallijn en indrukwekkende levelontwerp. Het gebruikt volledige lichaamsinverse kinematics (IK) technologie, waardoor spelers hun virtuele lichaam in real-time kunnen zien bewegen terwijl ze acties in het spel uitvoeren.";
    container.appendChild(h2);
    container.appendChild(p);
    document.body.appendChild(container);
    const boneworkscontainer = document.getElementById('boneworkscontainer');
    boneworkscontainer.style.animation = "fadeincontainer 0.2s cubic-bezier(0.39, 0.575, 0.565, 1) forwards"
    video.src = 'assets/boneworks.mp4';
    video.style.animation = "fadein 0.2s cubic-bezier(0.39, 0.575, 0.565, 1) forwards"

});


portal2.addEventListener('click', () => {
    removecontainers();
    const container = document.createElement('div');
    container.classList.add('container');
    container.id = 'portal2container';
    const h2 = document.createElement('h2');
    h2.textContent = 'Portal 2';
    const p = document.createElement('p');
    p.textContent = 'Portal 2 is een first-person puzzelvideogame ontwikkeld en gepubliceerd door Valve Corporation. Het werd uitgebracht op 19 april 2011 voor PC, PlayStation 3 en Xbox 360. Het is de opvolger van de eerste Portal-game en de eerste game van Valve die een E10+ rating kreeg, in tegenstelling tot de M-rating van hun vorige titels, met uitzondering van de eerste Portal-game en de originele Day of Defeat, die een T-rating hadden.';
    container.appendChild(h2);
    container.appendChild(p);
    document.body.appendChild(container);
    const portal2container = document.getElementById('portal2container');
    portal2container.style.animation = "fadeincontainer 0.2s cubic-bezier(0.39, 0.575, 0.565, 1) forwards"
    video.src = 'assets/portal2.mp4';
    video.style.animation = "fadein 0.2s cubic-bezier(0.39, 0.575, 0.565, 1) forwards"

});
video.style.opacity = 0;


function removecontainers()
{
    if(document.getElementById('portal2container'))
    {
        const portal2container = document.getElementById('portal2container');
        portal2container.style.animation = "fadeoutcontainer 0.2s cubic-bezier(0.39, 0.575, 0.565, 1) forwards"
        // wait 200ms
        setTimeout(() => {
            // remove the container
            document.getElementById('portal2container').remove();
        }, 200);
        // remove the container
        // return to prevent the creation of a new container
        video.style.animation = "fadeout 0.2s cubic-bezier(0.39, 0.575, 0.565, 1) forwards"
        return;
    }
    if(document.getElementById('boneworkscontainer'))
    {
        const boneworkscontainer = document.getElementById('boneworkscontainer');
        boneworkscontainer.style.animation = "fadeoutcontainer 0.2s cubic-bezier(0.39, 0.575, 0.565, 1) forwards"
        // wait 200ms
        setTimeout(() => {
            // remove the container
            document.getElementById('boneworkscontainer').remove();
        }, 200);
        // remove the container
        // return to prevent the creation of a new container
        video.style.animation = "fadeout 0.2s cubic-bezier(0.39, 0.575, 0.565, 1) forwards"
        return;
    }
    if(document.getElementById('minecraftcontainer'))
    {
        const minecraftcontainer = document.getElementById('minecraftcontainer');
        minecraftcontainer.style.animation = "fadeoutcontainer 0.2s cubic-bezier(0.39, 0.575, 0.565, 1) forwards"
        // wait 200ms
        setTimeout(() => {
            // remove the container
            document.getElementById('minecraftcontainer').remove();
        }, 200);
        // remove the container
        // return to prevent the creation of a new container
        video.style.animation = "fadeout 0.2s cubic-bezier(0.39, 0.575, 0.565, 1) forwards"
        return;
    }
    return;
}