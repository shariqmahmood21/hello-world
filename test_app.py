from app import app


def test_hello_world_get():
    response = app.test_client().get('/')
    assert response.status_code == 200
    assert response.data == b'<p>Hello, World</p>'


def test_hello_world_post():
    response = app.test_client().post('/')
    assert response.status_code == 200
    assert response.data == b'<p>Hello, World</p>'


def test_hello_world_get_header_json():
    response = app.test_client().get('/', headers={'X-accept-header': 'application/json'})
    assert response.status_code == 200
    assert response.data == b'{"message": "Hello, World"}'


def test_hello_world_get_header_xml():
    response = app.test_client().get('/', headers={'X-accept-header': 'application/xml'})
    assert response.status_code == 200
    assert response.data == b'<p>Hello, World</p>'
