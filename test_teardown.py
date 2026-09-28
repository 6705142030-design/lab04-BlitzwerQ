import pytest

@pytest.fixture
def resource():
    print("[setup]")
    yield "data"
    print("[teardown]")

def test_resource_value(resource):
    assert resource == "data"

def test_resource_is_string(resource):
    assert isinstance(resource, str)
