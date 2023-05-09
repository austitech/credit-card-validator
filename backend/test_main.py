from datetime import datetime

from fastapi.testclient import TestClient

from main import app
from service import luhn_algorithm_validator


client = TestClient(app)


def test_valid_credit_card():
    card_details = {
        "card_number": "4035501000000008",
        "expiry_year": datetime.now().year + 1,
        "expiry_month": datetime.now().month + 1,
        "cvv": "737",
    }
    response = client.post("/credit-card/validate", json=card_details)
    assert response.status_code == 200
    assert response.json() == {"message": "Credit card validated successfully"}


def test_invalid_card_number_with_luhn_algorithm():
    card_details = {
        "card_number": "4035501000000007",
        "expiry_year": datetime.now().year + 1,
        "expiry_month": datetime.now().month + 1,
        "cvv": "737",
    }
    response = client.post("/credit-card/validate", json=card_details)
    assert response.status_code == 400
    assert response.json() == {"detail": "Card number failed luhn algorithm check"}


def test_expired_credit_card():
    card_details = {
        "card_number": "4035501000000008",
        "expiry_year": datetime.now().year,
        "expiry_month": datetime.now().month,
        "cvv": "737",
    }
    response = client.post("/credit-card/validate", json=card_details)
    assert response.status_code == 400
    assert response.json() == {
        "detail": "Credit card expiration date is less than current time"
    }


def test_card_number_too_long():
    card_details = {
        "card_number": "40355010000000087089",
        "expiry_year": datetime.now().year + 1,
        "expiry_month": datetime.now().month + 1,
        "cvv": "737",
    }
    response = client.post("/credit-card/validate", json=card_details)
    assert len(card_details["card_number"]) > 19
    assert response.status_code == 400
    assert response.json() == {
        "detail": "Card number must be between 16 and 19 digits long"
    }


def test_card_number_too_short():
    card_details = {
        "card_number": "403550100000000",
        "expiry_year": datetime.now().year + 1,
        "expiry_month": datetime.now().month + 1,
        "cvv": "737",
    }
    response = client.post("/credit-card/validate", json=card_details)
    assert len(card_details["card_number"]) < 16
    assert response.status_code == 400
    assert response.json() == {
        "detail": "Card number must be between 16 and 19 digits long"
    }


def test_invalid_cvv_for_american_express_card():
    card_details_1 = {
        "card_number": "3782822463100058",
        "expiry_year": datetime.now().year + 1,
        "expiry_month": datetime.now().month + 1,
        "cvv": "737",
    }
    card_details_2 = {
        "card_number": "3482822463100058",
        "expiry_year": datetime.now().year + 1,
        "expiry_month": datetime.now().month + 1,
        "cvv": "737",
    }
    response_1 = client.post("/credit-card/validate", json=card_details_1)
    response_2 = client.post("/credit-card/validate", json=card_details_2)

    assert len(card_details_1["cvv"]) < 4
    assert len(card_details_2["cvv"]) < 4
    assert response_1.status_code == 400
    assert response_2.status_code == 400
    assert response_1.json() == {
        "detail": "CVV must be exactly 4 digits long for american express cards"
    }
    assert response_2.json() == {
        "detail": "CVV must be exactly 4 digits long for american express cards"
    }


def test_invalid_cvv_for_non_american_express_cards():
    card_details = {
        "card_number": "4035501000000008",
        "expiry_year": datetime.now().year + 1,
        "expiry_month": datetime.now().month + 1,
        "cvv": "73",
    }
    response = client.post("/credit-card/validate", json=card_details)
    assert len(card_details["cvv"]) < 3
    assert response.status_code == 400
    assert response.json() == {
        "detail": "CVV must be exactly 3 digits long for non american express cards"
    }


def test_luhn_algorithm_validator_on_invalid_card_number():
    invalid_card_number = "6011000990139425"
    result = luhn_algorithm_validator(invalid_card_number)
    assert result == False


def test_luhn_algorithm_validator_on_valid_card_number():
    valid_card_number = "6011000990139424"
    result = luhn_algorithm_validator(valid_card_number)
    assert result == True
