// Objetos en JS

const persona = {
  nombre: "Luis",
  edad: 30
};

// Notación con punto
console.log(persona.nombre); // "Luis"

// Notación con corchetes
console.log(persona["edad"]); // 30

// Agregar, modificar y eliminar propiedades
const coche = {
  marca: "Toyota",
  modelo: "Corolla"
};

// Agregar una nueva propiedad
coche.color = "Rojo";

// Modificar una existente
coche.modelo = "Yaris";

// Eliminar una propiedad
delete coche.marca;

console.log(coche);
