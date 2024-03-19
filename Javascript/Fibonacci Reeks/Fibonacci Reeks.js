// Functie om de Fibonacci-reeks te genereren
function fibonacci(n) {
    var fibArray = []; // Array om de Fibonacci-getallen op te slaan

    // Eerste twee Fibonacci-getallen zijn 0 en 1
    fibArray.push(0);
    fibArray.push(1);

    // Bereken de resterende Fibonacci-getallen en voeg ze toe aan de array
    for (var i = 2; i < n; i++) {
        fibArray.push(fibArray[i - 1] + fibArray[i - 2]);
    }

    return fibArray; // Return de array met Fibonacci-getallen
}

// Functie om de Fibonacci-getallen op het scherm te tonen
function displayFibonacci() {
    var fibNumbers = fibonacci(20); // Roep de fibonacci-functie op om de eerste 20 getallen te krijgen
    var output = "De eerste 20 getallen in de Fibonacci-reeks zijn: ";

    // Voeg elk Fibonacci-getal toe aan de uitvoerstring
    for (var i = 0; i < fibNumbers.length; i++) {
        output += fibNumbers[i] + ", ";
    }

    // Toon de uitvoer op het scherm
    console.log(output);
}

// Roep de functie aan om de Fibonacci-getallen weer te geven
displayFibonacci();