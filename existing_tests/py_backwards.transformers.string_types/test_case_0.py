import unittest
import timeout_decorator
import py_backwards.transformers.string_types as module_0

class Test_String_types_1(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        string_types_transformer_0 = module_0.StringTypesTransformer()

if __name__ == "__main__":
    unittest.main()
