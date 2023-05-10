from datetime import datetime
from fastapi import HTTPException, status


async def validate_credit_card(
    card_number: str, expiry_month: int, expiry_year: int, cvv: str
) -> bool:
    """Service for validating credit card information"""

    now = datetime.now()

    # Check that expiry year is greater than current year
    if now.year > expiry_year:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Credit card expiration date is less than current time",
        )
    else:
        # Check that expiry month is greater than current month
        # if expiry year equals current year
        if now.month >= expiry_month and expiry_year == now.year:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Credit card expiration date is less than current time",
            )

    # Check that card number is between 16 and 19 digits long
    card_number_length = len(card_number)
    if not (card_number_length >= 16 and card_number_length <= 19):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Card number must be between 16 and 19 digits long",
        )

    # Check that cvv is exactly 4 digits long for american express cards
    cvv_digits = len(cvv)
    if card_number[:2] in ["34", "37"] and cvv_digits != 4:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="CVV must be exactly 4 digits long for american express cards",
        )

    # Check that cvv is exactly 3 digits long for non american express cards
    if card_number[:2] not in ["34", "37"] and cvv_digits != 3:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="CVV must be exactly 3 digits long for non american express cards",
        )

    # Validate card_number last digit with luhn algorithm
    if luhn_algorithm_validator(card_number) == False:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Card number failed luhn algorithm check",
        )

    return True


def luhn_algorithm_validator(card_number: str) -> bool:
    """Luhn algorithm for validating credit card numbers"""

    luhn_sum = 0
    card_number_length = len(card_number)
    even_indexed = False

    for i in range(card_number_length - 1, -1, -1):
        if even_indexed == True:
            # multiply number by 2, add up the digits if product > 9 
            # then add it to luhn_sum
            number_doubled = int(card_number[i]) * 2
            if number_doubled > 9:
                number_doubled = sum(map(int, str(number_doubled)))
            luhn_sum += number_doubled
            even_indexed = not even_indexed
        else:
            luhn_sum += int(card_number[i])
            even_indexed = not even_indexed

    if luhn_sum % 10 == 0:
        return True
    else:
        return False
