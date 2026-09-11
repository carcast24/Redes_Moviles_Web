'''import json
with open("../data/clientes.json", "r", encoding="utf-8") as file: #encoding evita problemas si existen tildes o caracteres especiales dentro de nombres o el archivo
    clientes = json.load(file)

    for cliente in clientes: #recorremos la lista de diccionarios
        print(cliente["nombre"])

'''
import json
from fastapi import FastAPI
app = FastAPI()
@app.get("/")

def inicio():
    return {"Mensaje: Conexion API completada"}
#ejecute la api con el uvicorn
#uvicorn app.main:app --reload --host 127.0.0.1
@app.get("/clientes")
def llamar_clientes():
    with open("../data/clientes.json", "r", encoding="utf-8") as file:
        clientes = json.load(file)
    return clientes

