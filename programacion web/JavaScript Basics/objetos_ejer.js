// Crea un objeto llamado persona con las propiedades: nombre, edad, y ocupacion y Muestra en consola una frase con esa información.

const persona = {
  nombre: "Ana",
  edad: 25,
  ocupacion: "Ingeniera"
};

console.log(`${persona.nombre} tiene ${persona.edad} años y es ${persona.ocupacion}.`);

/*

Usando el objeto persona del ejercicio anterior:

Agrega una nueva propiedad llamada ciudad.

Cambia la propiedad ocupacion a otro valor.

Muestra el objeto actualizado.

*/

persona.ciudad = "Guadalajara";
persona.ocupacion = "Diseñadora";
console.log(persona);
