const url = 'http://127.0.0.1:8000/medicamentos/api/historial-medicamento/'
const res = document.getElementById('res')

fetch(url).then(function(response){
    return response.json()
}).then(function (data){
    console.log(data)
    res.innerHTML = ''
    
    data.forEach((dato) => {
        console.log(dato.medicine_id)
        res.innerHTML+= `
        <tr>
          <th>${dato.medicine_id.id}</th>
          <td>${dato.medicine_id.medicine_name}</td>
          <td>${dato.brand}</td>
        
        </tr>
        
        `


    });
})


