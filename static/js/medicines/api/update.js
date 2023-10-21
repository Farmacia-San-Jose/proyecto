
// OBTENIENDO EL ID DEL MEDICAMENTO A ACTUALIZAR 
var medicine_id = document.getElementById('medicine_id').value;

// Partes de formularios

// Medicamentos
var formulario_medicamento = document.getElementById('formulario_medicamento');

// Clasificacion
var checkbox_uso = document.getElementById('usoTerapeutico');
checkbox_uso.innerHTML='';

var checkbox_forma = document.getElementById('formaAdministracion');
checkbox_forma.innerHTML='';


// Detalle del medicamento
const url_medicamento = 'http://127.0.0.1:8000/medicamentos/api/medicamentos/'+medicine_id+'/'
const url_clasificacion = 'http://127.0.0.1:8000/clasificacion/api/v1/clasificacion/'
const url_uso_terapeutico = 'http://127.0.0.1:8000/clasificacion/api/v1/uso-terapeutico/'
const url_forma_administracion = 'http://127.0.0.1:8000/clasificacion/api/v1/forma-administracion/'



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
    formulario_medicamento.innerHTML += '<textarea name="medicine_description" id="medicine_description" class="form-control" rows="3" placeholder="Escribe la descripcion del medicamento" style="border: 1px solid #52be80;"></textarea value = "'+response.data.description+'">'

}).catch(function (error){
    // Manejar los errores
    console.error(error);
});

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
                checkbox_uso.innerHTML+='<div.class="form-group"> <div class="form-check"> <input checked class="form-check-input" type="checkbox" value="'+uso.id+'" id="'+uso.id+'name="opciones_uso[]" style="border:1px solid #52be80;"> <label class="form-check-label fw-medium" for="'+uso.id+'">'+uso.type_therepeuticuse+'</label></div></div>'
                
            }else{
                checkbox_uso.innerHTML+='<div.class="form-group"> <div class="form-check"><input  class="form-check-input" type="checkbox" value="'+uso.id+'" id="'+uso.id+'name="opciones_uso[]" style="border:1px solid #52be80;" ><label class="form-check-label fw-medium" for="'+uso.id+'">'+uso.type_therepeuticuse+'</label></div></div>'
            }

        });
        listado_forma_administracion.forEach(forma =>{
            if(listado_forma_administracion_seleccionado.includes(forma.id)){
                checkbox_forma.innerHTML+='<div.class="form-group"> <div class="form-check"> <input checked class="form-check-input" type="checkbox" value="'+forma.id+'" id="'+forma.id+'name="opciones_uso[]" style="border:1px solid #52be80;"> <label class="form-check-label fw-medium" for="'+forma.id+'">'+forma.type_adminstrationform+'</label></div></div>'
            }else{
                checkbox_forma.innerHTML+='<div.class="form-group"> <div class="form-check"> <input class="form-check-input" type="checkbox" value="'+forma.id+'" id="'+forma.id+'name="opciones_uso[]" style="border:1px solid #52be80;"> <label class="form-check-label fw-medium" for="'+forma.id+'">'+forma.type_adminstrationform+'</label></div></div>'
            }

        });


    })).catch(function(error){
        console.error(error);
    });


    


}


datos();





