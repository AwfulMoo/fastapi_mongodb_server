from fastapi_mongo_server import __version__


def test_version():
    assert __version__ == '1.0.0'
