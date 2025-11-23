import unittest
import timeout_decorator
import typesystem.schemas as module_0
import typesystem.fields as module_1

class Test_Schemas_22(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_8(self):
        str_0 = 'b'
        reference_0 = module_0.Reference(str_0)

if __name__ == "__main__":
    unittest.main()
