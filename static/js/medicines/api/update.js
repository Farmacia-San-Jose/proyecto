
const btn_actualizar = document.getElementById('btn_actualizar');


function verificarCheckboxes(checkboxes) {
    let contador = 0;
    for (var i = 0; i < checkboxes.length; i++) {
        if (checkboxes[i].checked) {
            console.log("Checkbox " + checkboxes[i].value + " está marcado.");
            
        } else {
            contador+=1;
            console.log("Checkbox " + checkboxes[i].value + " no está marcado.");
        }
    }
    console.log('CUANTOS NO HAY MARCADOS',contador);
    console.log('Total a marcar',checkboxes.length)
    
    if( contador == checkboxes.length ){
        
        return false;
    }
    return true;
    
}

console.log(document.getElementsByName('opciones_uso[]'));


btn_actualizar.addEventListener('click', function () {
    var usos = document.getElementsByName("opciones_uso[]");
    var formas = document.getElementsByName("opciones_forma[]");
    var mandar_resultado = document.getElementById('resultado');

        // Iterar a través de los checkboxes y verificar si están marcados
    let uso_select = verificarCheckboxes(usos);
    let forma_select = verificarCheckboxes(formas);

    if(!forma_select){
        alert('Usted no ha seleccionado ninguna Forma de Administracion, por favor seleccione uno')
    }
    if(!uso_select){
        alert('Usted no ha seleccionado ningun Uso Terapeutico, por favor seleccione uno')
    }
   
    if(forma_select && uso_select){
        mandar_resultado.value=true;
    }else{
        mandar_resultado.value=false;
    }

    
    
    
    
});