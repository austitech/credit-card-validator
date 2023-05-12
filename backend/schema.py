
from pydantic import BaseModel, validator


class CreditCardSchema(BaseModel):
    expiry_month: int
    expiry_year: int
    cvv: str
    card_number: str

    @validator("expiry_month", "expiry_year", "cvv", "card_number")
    def validate_all_fields_are_digits(cls, value):
        # try casting value to integer then fail on error
        # else return initial value
        try:
            int(value)
        except:
            raise ValueError("Value must be digits")
        
        return value
