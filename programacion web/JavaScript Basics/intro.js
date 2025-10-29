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
