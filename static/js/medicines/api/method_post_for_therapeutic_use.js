import {urls_external} from './urls.js';



function enviarDatos(){

    const tipo_uso = document.getElementById('tipo_uso_terapeutico').value;
    const descripcion_uso = document.getElementById('description_uso').value;

    

    const datos = {
        type_therepeuticuse: tipo_uso,
        description: descripcion_uso
    };

    const url_uso = urls_external.api_url_uso_terapeutico;

    axios.post(url_uso, datos, {
        headers:{
            'Authorization':`Token 58bab50f20e4d741cd2f606eb0297a8e64b7b263`
        }
    }).then(response =>{
        console.log('Respuesta del servidor: ', response.data);
    }).catch(error =>{
        console.error(error);
    });

    setTimeout(function(){
        console.log('Esperaaaa .....')
    }, 200000);


}



const bt_uso = document.getElementById('guardar_uso');

bt_uso.addEventListener('click', enviarDatos);