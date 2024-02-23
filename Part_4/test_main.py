from fastapi.testclient import TestClient
from .main import app
import pytest


@pytest.fixture
def client():
    yield TestClient(app)


def test_sample(client):
    assert True


# ========================================================================


@pytest.fixture
def client_autoclean_db(client):
    # calling delete API's to clear cars and owners table to give a empty table for unit test
    response = client.delete("/cars/")
    response = client.delete("/owners/")

    yield TestClient(app)


@pytest.fixture
def owner_value():
    return {"first_name": "Mickey", "last_name": "Mouse", "national_id": "SHJDK432432"}


@pytest.fixture
def bad_owner_value():
    return {"first_name": 12, "last_name": "Mouse", "national_id": "SHJDK432432"}


@pytest.fixture
def car_value():
    return {
        "plate_number": "HAS-531",
        "brand": "Toyota",
        "model": "Vitz",
        "year": 2012,
        "owner_id": 1,
    }


@pytest.fixture
def bad_car_value():
    return {
        "plate_number": "HAS-531",
        "brand": "Toyota",
        "model": "Vitz",
        "year": "2012",
        "owner_id": 1,
    }


@pytest.fixture
def carplate_value():
    return {"plate_number": "UWB-920"}


def test_post_owner_api(client_autoclean_db, owner_value, bad_owner_value):
    response = client_autoclean_db.post("/owners/", json=owner_value)
    output_value = response.json()

    # removing the "id"(owner_id) from json to compare with input given i.e, owner_value
    output_value.pop("id")
    assert response.status_code == 200 and output_value == owner_value

    # bad input by sending integer for first_name
    response = client_autoclean_db.post("/owners/", json=bad_owner_value)
    assert response.status_code == 422


def test_post_car_api(client_autoclean_db, car_value, bad_car_value):
    response = client_autoclean_db.post("/cars/", json=car_value)

    output_value = response.json()
    print(output_value)
    # removing the "id"(car_id) from json to compare with input given i.e, car_value
    output_value.pop("id")
    assert response.status_code == 200 and output_value == car_value

    # bad input by sending year as a string
    response = client_autoclean_db.post("/owners/", json=bad_car_value)
    assert response.status_code == 422


def test_get_owner_api(client_autoclean_db, owner_value, car_value):
    response = client_autoclean_db.post("/owners/", json=owner_value)
    assert response.status_code == 200
    print(response.json())

    response = client_autoclean_db.post("/cars/", json=car_value)
    assert response.status_code == 200
    print(response.json())

    # Success code for getting an existing value -> 200
    response = client_autoclean_db.get("/owners-full-details/1")
    assert response.status_code == 200
    print(response.json())

    # Detail not found code for a non existing value -> 404
    response = client_autoclean_db.get("/owners-full-details/12000")
    assert response.status_code == 404

    # Unprocessable entity code for sending a string instead of a number -> 422
    response = client_autoclean_db.get("/owners-full-details/rr")
    assert response.status_code == 422


def test_get_car_owner_api(client_autoclean_db, owner_value, car_value):
    response = client_autoclean_db.post("/owners/", json=owner_value)
    assert response.status_code == 200
    response = client_autoclean_db.post("/cars/", json=car_value)
    assert response.status_code == 200

    # Success code for getting an existing value -> 200
    response = client_autoclean_db.get("/cars-full-details/1")
    assert response.status_code == 200
    print(response.json())

    # Detail not found code for a non existing value -> 404
    response = client_autoclean_db.get("/cars-full-details/7899995")
    assert response.status_code == 404

    # Unprocessable entity code for sending a string instead of a number -> 422
    response = client_autoclean_db.get("/cars-full-details/AA")
    assert response.status_code == 422


def test_patch_car(client_autoclean_db, owner_value, car_value, carplate_value):
    response = client_autoclean_db.post("/owners/", json=owner_value)
    assert response.status_code == 200

    response = client_autoclean_db.post("/cars/", json=car_value)
    assert response.status_code == 200

    # Success code for sending a existing value
    response = client_autoclean_db.patch("/cars/1", json=carplate_value)
    output_value = response.json()
    chk_carplate = { "plate_number" : output_value["plate_number"] }
    assert response.status_code == 200 and chk_carplate == carplate_value

    # Detail not found code for a non exisitng value
    response = client_autoclean_db.patch("/cars/11222", json=carplate_value)
    assert response.status_code == 404


# ========================================================================
