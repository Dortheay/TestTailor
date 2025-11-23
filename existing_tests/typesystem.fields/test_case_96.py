import unittest
import timeout_decorator
import typesystem.fields as module_0
import decimal as module_1

class Test_Fields_97(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_11(self):
        array_0 = module_0.Array()
        any_0 = array_0.serialize(array_0)

if __name__ == "__main__":
    unittest.main()
