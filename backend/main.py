import uvicorn
from fastapi import FastAPI, status

import service
from schema import CreditCardSchema


app = FastAPI(
    title="Credit Card Validation API",
    description="API for fast validation of credit cards"
)


@app.post(
    "/credit-card/validate",
    status_code=status.HTTP_200_OK,
)
async def validate_credit_card(card_details: CreditCardSchema):
    """
    Validates credit card information
    -param expiry_month: credit card expiration month.
    -param expiry_year: credit card expiration year.
    -param card_number: digits between 16 and 19 digits long.
    -param cvv: exactly 3 digits long or 4 digits long for american express cards.
    """

    await service.validate_credit_card(
        card_number=card_details.card_number,
        expiry_month=card_details.expiry_month,
        expiry_year=card_details.expiry_year,
        cvv=card_details.cvv,
    )

    return {"message": "Credit card validated successfully"}


if __name__ == "__main__":
    uvicorn.run("main:app", port=7001)
