import unittest
import timeout_decorator
import py_backwards.transformers.variables_annotations as module_0

class Test_Variables_annotations_1(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        variables_annotations_transformer_0 = module_0.VariablesAnnotationsTransformer()

if __name__ == "__main__":
    unittest.main()
