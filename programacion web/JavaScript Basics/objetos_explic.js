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


