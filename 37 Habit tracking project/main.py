import requests
from data import USERNAME,GRAPH_ID,headers,params_3rd,params_4th


graph_endpoint = f"https://pixe.la/v1/users/{USERNAME}/graphs/{GRAPH_ID}/20220112"

response = requests.delete(url=graph_endpoint,headers=headers)
print(response.text)


