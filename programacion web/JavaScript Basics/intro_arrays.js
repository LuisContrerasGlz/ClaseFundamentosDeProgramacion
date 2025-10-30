// Arrays

// Iterar con For clasico 

const numeros = [10, 20, 30, 40];

for (let i = 0; i < numeros.length; i++) {
  console.log("Índice:", i, "→ Valor:", numeros[i]);
}

// Usando For of moderno

const numeros2 = [10, 20, 30, 40];

for (let n of numeros2) {
  console.log("Valor:", n);
}

// Sort y reverse

const nombres = ["Ana", "Luis", "Pedro"];
nombres.sort();     // ["Ana", "Luis", "Pedro"]
nombres.reverse();  // ["Pedro", "Luis", "Ana"]

// Concat slice

const a = [1, 2];
const b = [3, 4];
const c = a.concat(b); // [1, 2, 3, 4]

const parte = c.slice(1, 3); // [2, 3]

// Join

const palabras = ["Hola", "mundo"];
console.log(palabras.join(" ")); // "Hola mundo"

// filter and find

const edades = [12, 18, 25, 30];
const adultos = edades.filter(e => e >= 18);
const primerAdulto = edades.find(e => e >= 18);

console.log(adultos); // [18, 25, 30]
console.log(primerAdulto); // 18

// map

const nums = [1, 2, 3];
const doble = nums.map(n => n * 2);
console.log(doble); // [2, 4, 6]

// For each

const animales = ["Perro", "Gato", "Loro"];
animales.forEach(animal => console.log(animal));

// Index of and includes

const numeros3 = [5, 10, 15];
console.log(numeros3.indexOf(10)); // 1
console.log(numeros3.includes(20)); // false

// unshift and shift 
// unshift() agrega un elemento al inicio del arreglo.
// shift() elimina el primer elemento.

const letras = ["B", "C"];
letras.unshift("A");  // ["A", "B", "C"]
letras.shift();       // ["B", "C"]


