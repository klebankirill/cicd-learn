from hello import app

def test_hello_returns_greeting():
    client = app.test_client()
    response = client.get("/")
    assert response.status_code == 200
    assert "Hello" in response.data.decode("utf-8")
