from app import app


def test_hello_world():
    response = app.test_client().get('/')

    assert response.status_code == 200
    assert response.data == b'<p>Hello, World</p>'


def test_hello_world_2():
    response = app.test_client().post('/')

    assert response.status_code == 200
    assert response.data == b'<p>Hello, World</p>'


def test_hello_world_1():

    response = app.test_client().get('/',content_type = 'application/json')
    assert response.status_code == 200
    assert response.data == b'<p>Hello, World</p>'
