// Array met dagen van de week
var dagenVanDeWeek = ["maandag", "dinsdag", "woensdag", "donderdag", "vrijdag", "zaterdag", "zondag"];

// Functie om de dagen van de week in een leesbare string te converteren
function formatDagenVanDeWeek(dagenArray) {
    return dagenArray.join(", ");
}

// Functie om de dagen van de week in omgekeerde volgorde te krijgen
function omgekeerdeVolgorde(dagenArray) {
    return dagenArray.slice().reverse();
}

// Functie om de werkdagen van de week te krijgen
function werkdagen(dagenArray) {
    return dagenArray.slice(0, 5); // Maandag t/m vrijdag
}

// Functie om de weekenddagen van de week te krijgen
function weekenddagen(dagenArray) {
    return dagenArray.slice(5); // Zaterdag en zondag
}

// Kopje h2 "Alle dagen van de week zijn:"
console.log("<h2>Alle dagen van de week zijn:</h2>");
console.log(formatDagenVanDeWeek(dagenVanDeWeek));

// Kopje h2 "De werkdagen zijn:"
console.log("<h2>De werkdagen zijn:</h2>");
console.log(formatDagenVanDeWeek(werkdagen(dagenVanDeWeek)));

// Kopje h2 "De weekenddagen zijn:"
console.log("<h2>De weekenddagen zijn:</h2>");
console.log(formatDagenVanDeWeek(weekenddagen(dagenVanDeWeek)));

// Kopje h2 "Alle dagen van de week in omgekeerde volgorde zijn:"
console.log("<h2>Alle dagen van de week in omgekeerde volgorde zijn:</h2>");
console.log(formatDagenVanDeWeek(omgekeerdeVolgorde(dagenVanDeWeek)));

// Kopje h2 "De werkdagen in omgekeerde volgorde zijn:"
console.log("<h2>De werkdagen in omgekeerde volgorde zijn:</h2>");
console.log(formatDagenVanDeWeek(omgekeerdeVolgorde(werkdagen(dagenVanDeWeek))));

// Kopje h2 "De weekenddagen in omgekeerde volgorde zijn:"
console.log("<h2>De weekenddagen in omgekeerde volgorde zijn:</h2>");
console.log(formatDagenVanDeWeek(omgekeerdeVolgorde(weekenddagen(dagenVanDeWeek))));