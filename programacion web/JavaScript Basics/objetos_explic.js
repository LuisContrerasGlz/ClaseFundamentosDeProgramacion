const myKey = 'key';
const website = {
  name: 'AlgoExpert',
  rating: 5,
  founders: ['Clement', 'Antoine'],
  isAwesome: true,
  'multi word key': 0,
  [myKey]: 1234
};

console.log(website);

const website2 = {
  name: 'AlgoExpert',
  rating: 5,
  founders: ['Clement', 'Antoine']
};

console.log(website2.name);
console.log(website2['name']);
// Podemos usar [] cuando la key tenga espacios o caracteres entre ellos
console.log(website2['name for example test']);
console.log(website2['name_example_test']);
// Si queremos acceder a algo que no existe nos dara undefined 

// Aun que declaramos el objeto como const podemos modificar el contenido ya que no lo estamos redeclarando

website.name = 'FrontendExpert';
console.log(website.name);

website.foo = 'bar';
console.log(website);

delete website.foo;
console.log(website);

// También podemos crear objetos en JavaScript usando el constructor "new Object()".
// Ambas crean un objeto, pero esta usa la clase Object explícitamente.

const obj = new Object();
obj.name = 'Conner';
console.log(obj);

// Los Symbols son valores únicos en JavaScript, usados para crear propiedades de objeto que no se repiten.
// Aunque dos Symbols tengan la misma descripción, siempre son diferentes.
// Pueden usarse como claves en objetos sin riesgo de sobrescribir otras propiedades.

const id = Symbol('id');
const id2 = Symbol('id2');

console.log(id == id2); // false

const obj = {
  [id]: 1234,
  [id2]: 0,
  id: 'hello'
};

console.log(obj);

// Podemos verificar si una propiedad existe en un objeto de dos formas:
// 1. Con el operador "in" → revisa si la propiedad existe en el objeto o su prototipo.
// 2. Con "hasOwnProperty()" → revisa solo si la propiedad pertenece directamente al objeto.

console.log('name' in website);
console.log(website.hasOwnProperty('name'));

