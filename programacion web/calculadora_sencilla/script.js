let pantalla = document.getElementById('pantalla');

function agregar(valor) {
  pantalla.value += valor;
}

function calcular() {
  try {
    pantalla.value = eval(pantalla.value);
  } catch (error) {
    pantalla.value = "Error";
  }
}

function borrar() {
  pantalla.value = '';
}
