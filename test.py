import pytest
from app import app


@pytest.mark.parametrize(
    "path",
    [
        "/",
    ],
)
def test_routes(client, path):
    response = client.get(path)
    assert response.status_code == 200
    assert response.data == b"Hello, World!\n"
