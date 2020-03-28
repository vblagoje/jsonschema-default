import jsonschema_instance as js


def test_minimum():
    obj = js.create_from("./schemas/number/min.json")
    assert obj == {"number": 10}


def test_multipleof():
    obj = js.create_from("./schemas/number/multipleOf.json")
    assert obj == {"number": 11}
