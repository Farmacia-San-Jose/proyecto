// Listar todas las urls del API
import {urls, urls_external} from '../../urls/urls.js';

// Obtener el id de la transaccion a editar
const id_transaccion = document.getElementById('id_transaccion');
let id = id_transaccion.value;

// Lista que obtendra la informacion
const listar_seleccionados = []

// El body de la tabla
const table_body = document.getElementById('table_body');

let regi = [];
let registros = [];

export const select = (id)=>{
    let info = [];
    let infs = {};
    axios.all([
        axios.get(urls.api_url_historial_medicamento),
        axios.get(urls.api_url_historial_inventario)
    ]).then(axios.spread((response2, response3) => {        
        let listado_historial_medicamento = response2.data;
        let listado_historial_inventario = response3.data;

        listado_historial_medicamento.forEach(element => {
            if (element.medicine_id.id == id) {
                infs["medicine_id"] = element.medicine_id.id;
                infs["codigo"] = element.medication_code;
                infs["presentacion"] = element.presentation_id.presentation_type;
                infs["medicine_name"] = element.medicine_id.medicine_name;
            }
        });

        listado_historial_inventario.forEach(element => {
            if (element.medicine_id == id) {
                infs["sale_price"] = element.sale_price;
            }

        });
        info.push(infs);
        listar_tabla(infs);


    })).catch((err) => {
        console.error(err);

    });

};

// Obtener los datos antes seleccionados
export const listar = function(){

    axios.all([
        axios.get(urls.api_url_historial_transaccion+id+"/"),
        axios.get(urls.api_url_detalle_historial_transaccion)
    ]).then(axios.spread((response1, response2) =>{
        let detalle_transaccion = response2.data;
        
        detalle_transaccion.forEach(element => {
            if(element.transaction_id.id == id){  
                let datos = [];
                let seleccionados = [];             
                
                datos.push(element.medicine_id.id, element.medicine_id.medicine_name,element.price,element.quantity  )
                seleccionados.push(datos);
                organizarInformacion(seleccionados);
            }
        });
        


    })).catch((err)=>console.error(err));
}

// Organizar toda la informacion clave
function organizarInformacion(infor){
    
    infor.forEach((elements)=>{
        
        let id_medicine = elements[0];
       

        axios.get(urls.api_url_historial_medicamento).then((response)=>{
            let datos = response.data;
            datos.forEach((historial_medicamento)=>{
                if (historial_medicamento.medicine_id.id == id_medicine){
                    /*
                    console.log(historial_medicamento.medication_code);
                    console.log(historial_medicamento.presentation_id.presentation_type)
                    */
                    let organizado = []
                    let diccionario = {}
                    diccionario["codigo"]=historial_medicamento.medication_code;
                    diccionario["presentacion"]=historial_medicamento.presentation_id.presentation_type;
                    diccionario["medicine_id"]=elements[0];
                    diccionario["medicine_name"]=elements[1];
                    diccionario["sale_price"]=elements[2];
                    diccionario["cantidad"]=elements[3];
                    organizado.push(diccionario);
                    listar_tabla(diccionario);
                    
                }
            });

        }).catch((err)=>console.error(err));

        
    })
}

// Listar toda la informacion en la tabla
function listar_tabla(information){
    let imprimir = [];
    imprimir.push(information);
    regi.push(imprimir);
    
    
    imprimir.forEach((element, indice) =>{
        var nueva_fila = table_body.insertRow();
        var medication_code = nueva_fila.insertCell(0);
        medication_code.textContent = element.codigo;

        var medicine_name = nueva_fila.insertCell(1);
        medicine_name.textContent = element.medicine_name;
        var presentation_id = nueva_fila.insertCell(2);
        presentation_id.textContent = element.presentacion;

        var quantity = nueva_fila.insertCell(3);
        let inputQuantity = document.createElement("input");
        inputQuantity.type = "number";
        inputQuantity.id = "cantidad";
        inputQuantity.name = "cantidad";
        inputQuantity.min = "1";
        inputQuantity.style = "width:4rem; border:1px solid #52be80;";
        if(element.cantidad){
            inputQuantity.value = element.cantidad;
        }else{
            inputQuantity.value = 1;

        }
        
        quantity.appendChild(inputQuantity);

        var sale_price = nueva_fila.insertCell(4);
        let span_price = document.createElement("span")
        span_price.textContent =  parseFloat(element.sale_price).toFixed(2);
        sale_price.textContent = "Q ";
        sale_price.appendChild(span_price)

        var btn_remove = nueva_fila.insertCell(5);
        let btnDelete = document.createElement("button");
        btnDelete.textContent = "Eliminar";
        btnDelete.type = "button";
        btnDelete.style = "background-color:#52be80; color: #effaf3; border: 1px solid #52be80; border-radius: 2rem;"
        btn_remove.appendChild(btnDelete);

        btnDelete.addEventListener("click", function (event) {
            var fila = event.target.parentNode.parentNode;

            var tabla = fila.parentNode;

            tabla.removeChild(fila);
            regi.splice(indice, 1);

        });

        var id_me = nueva_fila.insertCell(6);
        let input_id_me = document.createElement('input');
        input_id_me.type = "hidden";
        input_id_me.value = element.medicine_id;
        id_me.appendChild(input_id_me)

    });
    
    
}

// Token 
function getCSRFToken() {
    const csrfCookieName = 'csrftoken'; // Nombre de la cookie CSRF en Django
    const cookieValue = document.cookie
        .split('; ')
        .find(cookie => cookie.startsWith(csrfCookieName))
        .split('=')[1];
    return cookieValue;
}

// Obtener la informacion de la tabla
function agrupar(){
    var filas = table_body.getElementsByTagName('tr');
    let listas = [];
    for(var i=0; i<filas.length; i++){
        
        var celdas = filas[i].getElementsByTagName('td');
        let medi_dic = {
            medicine_id:celdas[6].querySelector('input').value,
            cantidad:celdas[3].querySelector('input').value,
            sale_price:celdas[4].querySelector('span').textContent,

        };
        listas.push(medi_dic)

        
    }
    console.log(listas);
    registros.push(listas);

}

const enviar_transaccion = document.getElementById('miFormulario');

enviar_transaccion.addEventListener("submit", function (event) {
    const validar = document.getElementById('validar');
    
    
    agrupar()

    // EVITAR QUE SE RECARGUE LA PAGINA
    event.preventDefault();
    if (regi.length === 0) {
        alert("Usted no ha escogido ningun medicamento para el registro");
        validar.value = false;
    } else {
        validar.value = true;
        const csrf_token = getCSRFToken();        
        const transaction_date = document.getElementById('transaction_date');
        const transaction_type = document.getElementById('transaction_type');
        
        let url_edit = '/transaccion/editar/'+id+'/'
        console.log(url_edit);
        
        fetch(url_edit, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': csrf_token // Asegúrate de incluir el token CSRF si estás usando Django CSRF protection
            },
            body: JSON.stringify({lista:registros, validar:true,transaction_date:transaction_date.value,transaction_type: transaction_type.value})
        }).then(response => response.json()).then(data => {

            // Manejar la respuesta desde Django
            console.log("Manejar la respuesta...",data);
                
        }).catch(error => {
            console.error('Error:', error);
        });
        

        window.location.href = '/transaccion/';





    }
})