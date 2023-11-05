import {urls, urls_external} from '../../urls/urls.js';

const medicine_id = document.getElementById('medicine_id');
let id_medicine = medicine_id.value;

const formaAdministracion = document.getElementById('formaAdministracion');
const usoTerapeutico = document.getElementById('usoTerapeutico');

axios.all([
    axios.get(urls.api_url_clasificacion),
    axios.get(urls_external.api_url_forma_administracion),
    axios.get(urls_external.api_url_uso_terapeutico)
]).then(axios.spread(function(response1, response2, response3){
    let temp = [];
    let usoT = [];
    let formaA = [];
    let temp_uso = [];
    let temp_forma = [];

    temp = response1.data;
    formaA = response2.data;
    usoT = response3.data;

    temp.forEach(element => {
        if(element.medicine_id == id_medicine){
            temp_uso.push(element.therepeuticuse_id);
            temp_forma.push(element.formadministration_id);
        }
    });
    var crear_list_f = document.createElement("ul");
    var crear_list_u = document.createElement("ul");

    usoT.forEach((uso)=>{
        if(temp_uso.includes(uso.id)){
            var crear_li_u = document.createElement("li");
            crear_li_u.textContent = uso.type_therepeuticuse;
            crear_list_u.appendChild(crear_li_u)
        }

    });

    formaA.forEach((forma) =>{
        if(temp_forma.includes(forma.id)){
            var crear_li_f = document.createElement("li");
            crear_li_f.textContent = forma.type_adminstrationform;
            crear_list_f.appendChild(crear_li_f);

        }

    });
    formaAdministracion.appendChild(crear_list_f);
    usoTerapeutico.appendChild(crear_list_u)


})).catch((error)=>{
    console.error(error);
});