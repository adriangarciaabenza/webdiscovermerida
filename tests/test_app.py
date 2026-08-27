from app import app


def test_homepage_returns_hello_world():
    with app.test_client() as client:
        response = client.get("/")

    assert response.status_code == 200
    assert b"Hello, World!" in response.data


def test_homepage_links_to_merida():
    with app.test_client() as client:
        response = client.get("/")

    assert b">Descubre M\xc3\xa9rida</a>" in response.data
    assert b'href="/merida"' in response.data


def test_merida_page_contains_historical_context_and_home_link():
    with app.test_client() as client:
        response = client.get("/merida")

    assert response.status_code == 200
    assert b"M\xc3\xa9rida" in response.data
    assert b"Extremadura" in response.data
    assert b"romanos" in response.data
    assert b'href="/"' in response.data


def test_merida_page_contains_visit_guide_and_local_images():
    with app.test_client() as client:
        response = client.get("/merida")

    assert b"Qu\xc3\xa9 ver y visitar" in response.data
    for place in ("Teatro Romano", "Anfiteatro Romano", "Puente Romano",
                  "Acueducto de los Milagros", "Museo Nacional de Arte Romano"):
        assert place.encode("utf-8") in response.data
    assert response.data.count(b"/static/images/") == 6
    assert b".jpg" in response.data
    assert response.data.count(b"alt=") >= 6
