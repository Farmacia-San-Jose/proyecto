
// OBTENIENDO EL ID DEL MEDICAMENTO A ACTUALIZAR 
var medicine_id = document.getElementById('medicine_id').value;
const selector_proveedor = document.getElementById('proveedor_select');
selector_proveedor.innerHTML = '';

// Partes de formularios

// Medicamentos
var formulario_medicamento = document.getElementById('formulario_medicamento');

// Clasificacion
var checkbox_uso = document.getElementById('usoTerapeutico');
checkbox_uso.innerHTML='';

var checkbox_forma = document.getElementById('formaAdministracion');
checkbox_forma.innerHTML='';

// Precios
var cost_price = document.getElementById('cost_price');
var sale_price = document.getElementById('sale_price');

// Marca
var brand = document.getElementById('brand');

// Codigo
var code_medicine = document.getElementById('code_medicine');

// Cantidad
var cantidad = document.getElementById('cantidad');

// Fecha
var fecha = document.getElementById('fecha');

var presentacion = document.getElementById('presentacion');
presentacion.innerHTML = '';

// seccion
var seccion = document.getElementById('seccion');
seccion.innerHTML='';
const ubicacion = document.getElementById('ubicacions');
ubicacion.innerHTML='';
var fila = document.getElementById('fila');
var columna = document.getElementById('column');

// Detalle del medicamento
const url_medicamento = 'http://127.0.0.1:8000/medicamentos/api/medicamentos/'+medicine_id+'/'
const url_clasificacion = 'http://127.0.0.1:8000/clasificacion/api/v1/clasificacion/'
const url_uso_terapeutico = 'http://127.0.0.1:8000/clasificacion/api/v1/uso-terapeutico/'
const url_forma_administracion = 'http://127.0.0.1:8000/clasificacion/api/v1/forma-administracion/'
const url_proveedor = 'http://127.0.0.1:8000/proveedor/api/proveedor/'
const url_presentacion = 'http://127.0.0.1:8000/presentacion/api/presentacion/'

const url_historial_medicamento = 'http://127.0.0.1:8000/medicamentos/api/historial-medicamento/'
const url_historial_inventario = 'http://127.0.0.1:8000/ubicacion/api/v1/historial_inventario/'
const url_seccion = 'http://127.0.0.1:8000/ubicacion/api/v1/seccion/'
const url_ubicacion = 'http://127.0.0.1:8000/ubicacion/api/v1/ubicacion/'


// Informacion del medicamento
axios.get(url_medicamento).then(function (response){
    // Datos que envia el servidor

    formulario_medicamento.innerHTML = '<div class="form-group">'
    formulario_medicamento.innerHTML += '<label for="medicine_name" class="fw-medium">Nombre del Medicamento</label>'
    formulario_medicamento.innerHTML += ' <input type="text" id="medicine_name" name="medicine_name" class="form-control" required placeholder="Escribre el nombre del medicamento" style="border: 1px solid #52be80;"'+'value = "'+response.data.medicine_name+'">'
    formulario_medicamento.innerHTML += '</div>'
    formulario_medicamento.innerHTML += '<br>'
    formulario_medicamento.innerHTML += '<div class="form-group">'
    formulario_medicamento.innerHTML += '<label for="description" class="fw-medium">Descripcion del Medicamento</label>'
    formulario_medicamento.innerHTML += '<textarea name="medicine_description" id="medicine_description" class="form-control" rows="3" placeholder="Escribe la descripcion del medicamento" style="border: 1px solid #52be80;"></textarea>'

    let temp = [];
    temp.push(response.data);
    let descriptcion = document.getElementById('medicine_description');
    temp.forEach(me =>{
        descriptcion.value = me.description;


    });
  

}).catch(function (error){
    // Manejar los errores
    console.error(error);
});

// Informacion segun su clasificacion
function datos (){
    let listado_uso_terapeutico = []
    let listado_forma_administracion = []
    let listado_uso_terapeutico_seleccionado = []
    let listado_forma_administracion_seleccionado = []
    let listado_clasificacion = []
    axios.all([
        axios.get(url_clasificacion),
        axios.get(url_uso_terapeutico),
        axios.get(url_forma_administracion)
    ]).then(axios.spread(function(response1, response2, response3){
        let temp = [];
        
        temp = response1.data;
        listado_uso_terapeutico = response2.data;
        listado_forma_administracion = response3.data;

        // FILTRAR LOS SELECCIONADOS
        temp.forEach(cla =>{
            if(cla.medicine_id == medicine_id){
                listado_uso_terapeutico_seleccionado.push( cla.therepeuticuse_id);
                listado_forma_administracion_seleccionado.push(cla.formadministration_id);
            }
        });
        listado_uso_terapeutico.forEach(uso => {           
            if(listado_uso_terapeutico_seleccionado.includes(uso.id)){
                checkbox_uso.innerHTML+='<div.class="form-group"> <div class="form-check"> <input checked class="form-check-input" type="checkbox" value="'+uso.id+'" id="opciones_uso[]" name="opciones_uso[]" style="border:1px solid #52be80;"> <label class="form-check-label fw-medium" for="'+uso.id+'">'+uso.type_therepeuticuse+'</label></div></div>'
                
            }else{
                checkbox_uso.innerHTML+='<div.class="form-group"> <div class="form-check"><input  class="form-check-input" type="checkbox" value="'+uso.id+'" id="opciones_uso[]" name="opciones_uso[]" style="border:1px solid #52be80;" ><label class="form-check-label fw-medium" for="'+uso.id+'">'+uso.type_therepeuticuse+'</label></div></div>'
            }

        });
        listado_forma_administracion.forEach(forma =>{
            if(listado_forma_administracion_seleccionado.includes(forma.id)){
                checkbox_forma.innerHTML+='<div.class="form-group"> <div class="form-check"> <input checked class="form-check-input" type="checkbox" value="'+forma.id+'" id="opciones_forma[]" name="opciones_forma[]" style="border:1px solid #52be80;"> <label class="form-check-label fw-medium" for="'+forma.id+'">'+forma.type_adminstrationform+'</label></div></div>'
            }else{
                checkbox_forma.innerHTML+='<div.class="form-group"> <div class="form-check"> <input class="form-check-input" type="checkbox" value="'+forma.id+'" id="opciones_forma[]" name="opciones_forma[]" style="border:1px solid #52be80;"> <label class="form-check-label fw-medium" for="'+forma.id+'">'+forma.type_adminstrationform+'</label></div></div>'
            }

        });


    })).catch(function(error){
        console.error(error);
    });


    


}


datos();

function datos2(){
    // Historial de medicamento
    let listado_historial_medicamento = [];
    //Historial de inventario
    let listado_historial_inventario = [];
    // Presentacion
    let listado_presentacion = [];
    let presentacion_seleccionado =[];
    // Proveedor
    let proveedor_list_select = [];
    let proveedor_list = [];
    // Ubicacion
    let ubicaicon_list =[];
    let ubicacion_select = [];
    // Seccion
    let seccion_list = [];
    let seccion_select = [];
    
    axios.all([
        axios.get(url_historial_medicamento),
        axios.get(url_historial_inventario),
        axios.get(url_presentacion),
        axios.get(url_proveedor),
        axios.get(url_seccion),
        axios.get(url_ubicacion)
    ])
    .then(axios.spread((response, response2, response3, response4, response5, response6)=>{
        listado_historial_medicamento = response.data;
        listado_historial_inventario = response2.data;
        listado_presentacion = response3.data;
        proveedor_list = response4.data;
        ubicaicon_list = response6.data;
        seccion_list = response5.data;

        // HISTORIAL DE MEDICAMENTO
        listado_historial_medicamento.forEach(historial =>{
            if(historial.medicine_id.id == medicine_id){
                cost_price.value = historial.cost_price;
                brand.value = historial.brand;
                code_medicine.value = historial.medication_code;
                fecha.value = historial.expiration_date;
                presentacion_seleccionado.push( historial.presentation_id.id);
                proveedor_list_select.push(historial.supplier_id.id);
            }
        });

        // HISTORIAL DE INVENTARIO
        listado_historial_inventario.forEach(inventario =>{
            if( inventario.medicine_id == medicine_id){
                sale_price.value = inventario.sale_price;
                cantidad.value = inventario.quantity_stock;
                fila.value = inventario.row;
                columna.value = inventario.column;
                seccion_select.push(inventario.locationsection_id);
                ubicacion_select.push(inventario.location_id);


            }
        });

        // LISTADO DE PRESENTACIONES
        listado_presentacion.forEach(presentations=>{
            if(presentacion_seleccionado.includes(presentations.id)){
                presentacion.innerHTML+="<div class='form-group'> <div class='form-check'> <input checked type='radio' class='form-check-input' value='"+presentations.id+"' id='tipo_presentacion' name='tipo_presentacion' style='border: 1px solid #52be80;'> <label class='form-check-label fw-medium' for='"+presentations.id+"' >"+presentations.presentation_type+ "</label></div></div>"
            }else{
                presentacion.innerHTML+="<div class='form-group'> <div class='form-check'> <input type='radio' class='form-check-input' value='"+presentations.id+"' id='tipo_presentacion' name='tipo_presentacion' style='border: 1px solid #52be80;'> <label class='form-check-label fw-medium' for='"+presentations.id+"' >"+presentations.presentation_type+ "</label></div></div>"
            }

        });


        // Listado de proveedores
        proveedor_list.forEach(supplier=>{
            if(proveedor_list_select.includes(supplier.id)){
                if (supplier.last_name === null){
                    selector_proveedor.innerHTML+="<option selected value='"+supplier.id+"'>"+ supplier.first_name+"</option>"
                }else{
                    selector_proveedor.innerHTML+="<option selected value='"+supplier.id+"'>"+ supplier.first_name+" "+supplier.last_name+"</option>"
                }
                
            }else{
                if (supplier.last_name === null){
                    selector_proveedor.innerHTML+="<option value='"+supplier.id+"'>"+ supplier.first_name+"</option>"
                }else{
                    selector_proveedor.innerHTML+="<option value='"+supplier.id+"'>"+ supplier.first_name+" "+supplier.last_name+"</option>"
                }
            }

        });

        ubicaicon_list.forEach(location =>{
            if(ubicacion_select.includes(location.id)){
                ubicacion.innerHTML+="<option selected value='"+location.id+"'>"+ location.type_location+"</option>"
            }else{
                ubicacion.innerHTML+="<option value='"+location.id+"'>"+ location.type_location+"</option>"
            }

        });
        seccion_list.forEach(section => {
            if( seccion_select.includes(section.id)){
                seccion.innerHTML+="<option selected value='"+section.id+"'>"+ section.location_section+"</option>"
            }else{
                seccion.innerHTML+="<option value='"+section.id+"'>"+ section.location_section+"</option>"
            }


        });


    })).catch( function(error){
        console.error(error);
    });
}

datos2();

$(document).ready(function() {
    $('.js-example-basic-single').select2();
});



