from fastapi import FastAPI
from ..service.get_cotizaciones import GetAllCotizaciones

app = FastAPI()

@app.get("/")
def get_index():
    service = GetAllCotizaciones()
    return {'message': service.get_all()}
