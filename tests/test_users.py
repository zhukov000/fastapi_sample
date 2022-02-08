from starlette.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_users_read():
    resonse = client.get("/users")
    assert resonse.status_code == 200


"""
if __name__ == 'main':
    # pytest.main()
    pass
"""