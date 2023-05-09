
from pydantic import BaseModel


class CreditCardSchema(BaseModel):
    expiry_month: int
    expiry_year: int
    cvv: str
    card_number: str
