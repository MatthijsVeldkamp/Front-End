var dagenVanDeWeek = ["maandag", "dinsdag", "woensdag", "donderdag", "vrijdag", "zaterdag", "zondag"];

function formatDagenVanDeWeek(dagenArray) {
    return dagenArray.join(", ");
}

function omgekeerdeVolgorde(dagenArray) {
    return dagenArray.slice().reverse();
}

function werkdagen(dagenArray) {
    return dagenArray.slice(0, 5);
}

function weekenddagen(dagenArray) {
    return dagenArray.slice(5);
}

console.log("<h2>Alle dagen van de week zijn:</h2>");
console.log(formatDagenVanDeWeek(dagenVanDeWeek));

console.log("<h2>De werkdagen zijn:</h2>");
console.log(formatDagenVanDeWeek(werkdagen(dagenVanDeWeek)));

console.log("<h2>De weekenddagen zijn:</h2>");
console.log(formatDagenVanDeWeek(weekenddagen(dagenVanDeWeek)));

console.log("<h2>Alle dagen van de week in omgekeerde volgorde zijn:</h2>");
console.log(formatDagenVanDeWeek(omgekeerdeVolgorde(dagenVanDeWeek)));

console.log("<h2>De werkdagen in omgekeerde volgorde zijn:</h2>");
console.log(formatDagenVanDeWeek(omgekeerdeVolgorde(werkdagen(dagenVanDeWeek))));

console.log("<h2>De weekenddagen in omgekeerde volgorde zijn:</h2>");
console.log(formatDagenVanDeWeek(omgekeerdeVolgorde(weekenddagen(dagenVanDeWeek))));