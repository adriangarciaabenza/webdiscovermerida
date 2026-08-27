from app import app


def test_homepage_returns_hello_world():
    with app.test_client() as client:
        response = client.get("/")

    assert response.status_code == 200
    assert b"Hello, World!" in response.data
