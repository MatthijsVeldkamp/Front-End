var amtofnumbers = 20;

function generateFibonacci(amtofnumbers)
{
    var fib = [];
    fib[0] = 0;
    fib[1] = 1;
    for (var i = 2; i < amtofnumbers+1; i++)
    {
        fib[i] = fib[i-1] + fib[i-2];
    }
    return fib;
}

function displayFibonacci(fib)
{
    for (var i = 0; i < fib.length; i++)
    {
        console.log(fib[i]);
    }
}

var fib = generateFibonacci(amtofnumbers);
displayFibonacci(fib);