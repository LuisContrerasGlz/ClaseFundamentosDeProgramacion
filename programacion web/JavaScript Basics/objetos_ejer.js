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

/*
Crea un objeto auto con propiedades marca, modelo y año.
Usa un ciclo for...in para mostrar cada propiedad y su valor.
*/

const auto = {
  marca: "Toyota",
  modelo: "Yaris",
  año: 2022
};

for (let propiedad in auto) {
  console.log(propiedad + ": " + auto[propiedad]);
}

/*
Crea un objeto rectangulo con las propiedades ancho y alto,
y un método area() que calcule y devuelva el área.
*/

const rectangulo = {
  ancho: 5,
  alto: 3,
  area: function() {
    return this.ancho * this.alto;
  }
};

console.log("Área del rectángulo:", rectangulo.area());
