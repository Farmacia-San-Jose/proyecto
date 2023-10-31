
const user_id = document.getElementById('user_id')
const user = document.getElementById('user')

user_id.value = user.value
$(document).ready(function(){
    $('.medi').select2({
        
        placeholder:'Selecione un medicamento',
        allowClear:true
        
    });
})