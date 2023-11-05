
const user_id = document.getElementById('user_id')
const user = document.getElementById('user')
user_id.value = user.value;



 
const seleccionar = document.getElementById('seleccionar');


import {table_list} from './table.js';

seleccionar.addEventListener('click', function(){
    var select_medicamento = document.getElementById('select_medicamento');
    var valor_seleccionado = select_medicamento.value;

    if (valor_seleccionado != 0 || valor_seleccionado != "0"){    
        table_list(valor_seleccionado);
    }else{
        console.log("Debe de seleccionar un dato");
    }
});










$(document).ready(function(){
    $('.medi').select2();
});
