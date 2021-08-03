from pydantic import BaseModel

class CotizacionBase(BaseModel):
    exchange: str
    precio: float
    moneda: str
    volumen: float

class Cotizacion(CotizacionBase):
    is_active=bool

    class Config:
        orm_mode=True
