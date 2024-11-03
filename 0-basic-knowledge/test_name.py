from json_load import get_name

def test_get_name():
    name = get_name()
    assert name == 'name'