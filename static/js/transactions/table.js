import { urls, urls_external } from '../urls/urls.js';
const table_body = document.getElementById('table_body');

let regi = [];
let registros = [];

// Agrupando todos los medicamento que estan siento seleccionados
export const table_list = (id) => {
    let medicines = urls.api_url_medicamento + id + '/';
    let info = [];
    let infs = {};
    axios.all([
        axios.get(medicines),
        axios.get(urls.api_url_historial_medicamento),
        axios.get(urls.api_url_historial_inventario)
    ]).then(axios.spread((response1, response2, response3) => {
        let list_medicines = response1.data;
        let listado_historial_medicamento = response2.data;
        let listado_historial_inventario = response3.data;

        listado_historial_medicamento.forEach(element => {
            if (element.medicine_id.id == id) {
                infs["medicine_id"] = element.medicine_id.id;
                infs["medication_code"] = element.medication_code;
                infs["presentation_id"] = element.presentation_id.presentation_type;
                infs["medicine_name"] = element.medicine_id.medicine_name;
            }
        });

        listado_historial_inventario.forEach(element => {
            if (element.medicine_id == id) {
                infs["sale_price"] = element.sale_price;
            }

        });
        info.push(infs);
        listar(info);


    })).catch((err) => {
        console.error(err);

    });

}

// LISTAR TODOS LOS MEDICAMENTOS SELECCIONADOS
function listar(d) {
    regi.push(d);
    table_body.innerHTML = "";
    
    
    var tabla = document.getElementById("miTabla");

    regi.forEach((elements, indice) => {
        var nuevaFila = table_body.insertRow();
        elements.forEach((element) => {

            var medication_code = nuevaFila.insertCell(0);
            medication_code.textContent = element.medication_code;

            var medicine_name = nuevaFila.insertCell(1);
            medicine_name.textContent = element.medicine_name;

            var presentation_id = nuevaFila.insertCell(2);
            presentation_id.textContent = element.presentation_id;

            var quantity = nuevaFila.insertCell(3);
            let inputQuantity = document.createElement("input");
            inputQuantity.type = "number";
            inputQuantity.id = "cantidad";
            inputQuantity.name = "cantidad";
            inputQuantity.min = "1";
            inputQuantity.style = "width:4rem; border:1px solid #52be80;";
            inputQuantity.value = "1";
            quantity.appendChild(inputQuantity);
            

            var sale_price = nuevaFila.insertCell(4);
            let span_price = document.createElement("span")
            span_price.textContent = element.sale_price;
            sale_price.textContent = "Q ";
            sale_price.appendChild(span_price)


            var btn_remove = nuevaFila.insertCell(5);
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

            var id_me = nuevaFila.insertCell(6);
            let input_id_me = document.createElement('input');
            input_id_me.type = "hidden";
            input_id_me.value = element.medicine_id;
            id_me.appendChild(input_id_me)
        });
    });
    

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

function getCSRFToken() {
    const csrfCookieName = 'csrftoken'; // Nombre de la cookie CSRF en Django
    const cookieValue = document.cookie
        .split('; ')
        .find(cookie => cookie.startsWith(csrfCookieName))
        .split('=')[1];
    return cookieValue;
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
        

        fetch('/transaccion/realizar_transaccion/', {
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


