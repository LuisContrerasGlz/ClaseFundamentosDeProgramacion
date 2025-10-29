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
