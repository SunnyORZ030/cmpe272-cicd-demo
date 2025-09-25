from app import app
def test_root_returns_hello():
    client = app.test_client()
    r = client.get("/")
    assert r.status_code == 200
    assert b"hello" in r.data
