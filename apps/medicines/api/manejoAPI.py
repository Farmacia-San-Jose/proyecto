import requests
from django.http import JsonResponse
url = "http://127.0.0.1:8000/medicamentos/api/medicamentos/"
headers = {
        'Accept':'application/json; indent=4'
    }
try:
    response = requests.get(url, headers=headers,auth=('choc1403','choc1403'))

    if response.status_code==200:
        data = response.json()
        respuesta = []
        respuesta.append(data)
        dic = {"dato":respuesta}
        JsonResponse(dic)
    else:
        JsonResponse({'error': 'Error al consumir la API'}, status=response.status_code)
        
except Exception as e:
    JsonResponse({'error':str(e)}, status=500)