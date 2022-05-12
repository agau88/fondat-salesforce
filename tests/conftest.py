import pytest


def pytest_addoption(parser):
    parser.addoption(
        "--auth", action="store", default="password", help="auth: password|refresh"
    )


@pytest.fixture(scope="module")
def auth_type(request):
    return request.config.getoption("--auth")
