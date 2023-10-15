import pytest
import respx
from httpx import Response

from vanty.config import config


@pytest.fixture
def mocked_api():
    server_url = config.get("server_url")

    with respx.mock(base_url=server_url, assert_all_called=False) as respx_mock:
        # Mock the `verify` method
        respx_mock.post("/projects/authenticate-token/").mock(
            return_value=Response(
                200,
                json={
                    "is_valid": True,
                    "token_id": "test_token_id",
                    "token_secret": "test_token_secret",
                },
            )
        )

        # Mock the `download` method
        respx_mock.get("/projects/").mock(
            return_value=Response(
                200,
                json={
                    "is_valid": True,
                    "profile_status": "active",
                    "url": f"{server_url}/test.zip",
                },
            )
        )

        # Mock the `_download_zip` method
        respx_mock.get(f"{server_url}/test.zip").mock(
            return_value=Response(200, content=b"Test zip content")
        )

        yield respx_mock
