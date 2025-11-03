// Crea un programa que recorra un arreglo de números y calcule la suma total de todos sus elementos.

const numeros = [3, 7, 2, 9];
let suma = 0;

for (let i = 0; i < numeros.length; i++) {
  suma += numeros[i];
}

console.log("La suma total es " + suma);

// Crea un programa que recorra un arreglo de números y separe los pares e impares en dos nuevos arreglos.

const numeros2 = [10, 5, 8, 3, 2];
const pares = [];
const impares = [];

for (let n of numeros2) {
  if (n % 2 === 0) {
    pares.push(n);
  } else {
    impares.push(n);
  }
}

console.log("Pares:", pares);
console.log("Impares:", impares);

// Crea un programa que muestre el arreglo invertido, sin usar el método reverse().

const original = [1, 2, 3, 4, 5];
const invertido = [];

for (let i = original.length - 1; i >= 0; i--) {
  invertido.push(original[i]);
}

console.log(invertido);

// Crea un programa que reciba un arreglo de números y un número límite.
// El programa debe mostrar solo los números que sean mayores al límite.

const numeros3 = [5, 12, 8, 130, 44];
const limite = 10;
const mayores = [];

for (let n of numeros3) {
  if (n > limite) {
    mayores.push(n);
  }
}

console.log("Números mayores a " + limite + ": " + mayores);
