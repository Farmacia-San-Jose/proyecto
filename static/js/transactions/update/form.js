$(document).ready(function(){
    $('.medi').select2();
});


const user_id = document.getElementById('user_id')
const user = document.getElementById('user')
user_id.value = user.value;
const seleccionar = document.getElementById('seleccionar');


import {listar, select} from './tabla.js';
listar();

seleccionar.addEventListener('click', function(event){
    event.preventDefault();
    var select_medicamento = document.getElementById('select_medicamento');
    var valor_seleccionado = select_medicamento.value;

    if (valor_seleccionado != 0 || valor_seleccionado != "0"){    
        select(valor_seleccionado);
    }else{
        console.log("Debe de seleccionar un dato");
    }
});