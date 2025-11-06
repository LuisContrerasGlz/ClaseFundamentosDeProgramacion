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



