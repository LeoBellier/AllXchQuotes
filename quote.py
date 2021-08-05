from pydantic import BaseModel


class QuotesBase(BaseModel):
    exchange: str
    price: float
    coin: str
    volume: float


class Quotes(QuotesBase):
    is_active = bool

    class Config:
        orm_mode = True
