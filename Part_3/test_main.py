from fastapi.testclient import TestClient
from .main import app
import pytest


@pytest.fixture
def client():
    yield TestClient(app)


def test_sample(client):
    assert True


# ========================================================================
from .main import messages


@pytest.fixture
def client_new():
    yield TestClient(app)
    
    # clears the messages in the dict
    global messages
    messages.clear()


@pytest.fixture
def input_text():
    return "Hello World"


@pytest.fixture
def new_input_text():
    return "Beautiful World"


def test_post_sample(client_new, input_text):
    # Sucessful test -> 200
    response = client_new.post(f"/message?message={input_text}")
    assert response.status_code == 200
    assert response.json() == f"{input_text}: Saved successfully "

    # test with wrong query parameter mess instead of message -> 422
    response = client_new.post(f"/message?mess={input_text}")
    assert response.status_code == 422


def test_get_sample(client_new, input_text):
    # testing for an empty dict -> 404
    response = client_new.get(f"/message/message_1")
    assert response.status_code == 404 and response.json() == {
        "detail": "Message not found"
    }

    response = client_new.post(f"/message?message={input_text}")
    assert response.status_code == 200

    # Sucessful test -> 200
    response1 = client_new.get(f"/message/message_1")
    assert response1.status_code == 200
    assert response1.json() == input_text

    # test of message not in dict ->404
    response1 = client_new.get(f"/message/mesage_1")
    assert response1.status_code == 404 and response1.json() == {
        "detail": "Message not found"
    }


def test_get_all_sample(client_new, input_text):
    # to test an empty message -> 404
    response = client_new.get("/")
    assert response.status_code == 404 and response.json() == {
        "detail": "There is no message"
    }

    response = client_new.post(f"/message?message={input_text}")
    assert response.status_code == 200

    response = client_new.post(f"/message?message=My world is beautiful")
    assert response.status_code == 200

    response1 = client_new.get("/")
    assert response1.status_code == 200

    assert response1.json() == {
        "message_1": "Hello World",
        "message_2": "My world is beautiful",
    }


def test_patch_sample(client_new, input_text, new_input_text):
    response = client_new.post(f"/message?message={input_text}")
    assert response.status_code == 200

    response = client_new.patch(f"/message/message_1?new_message={new_input_text}")
    assert response.status_code == 200
    assert response.json() == new_input_text

    # testing for trying to patch a message not found in the dict
    response = client_new.patch(f"/message/wrong_message_1?new_message={new_input_text}")
    assert response.status_code == 404 and response.json() == {
        "detail": "Message not found"
    }


def test_delete_sample(client_new,input_text):
    response = client_new.post(f"/message?message={input_text}")
    assert response.status_code == 200

    response = client_new.delete(f"/message/message_1")
    assert (
        response.status_code == 200
        and response.json() == "message_1: Successfully deleted "
    )

    response = client_new.delete(f"/message/message_1")
    assert response.status_code == 404 and response.json() == {
        "detail": "Message not found"
    }
    
# ========================================================================
