from src.infer.type_inferrer import TypeInferrer

def test_type_inference():
    assert TypeInferrer.infer_type(["1", "25", "-99"]) == "integer"
    assert TypeInferrer.infer_type(["1.5", "25.0", "-0.99"]) == "float"
    assert TypeInferrer.infer_type(["True", "false", "yes"]) == "boolean"
    assert TypeInferrer.infer_type(["alpha", "123", "beta"]) == "string"
