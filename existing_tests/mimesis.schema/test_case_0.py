import unittest
import timeout_decorator
import mimesis.schema as module_0

class Test_Schema_1(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        abstract_field_0 = module_0.AbstractField()

if __name__ == "__main__":
    unittest.main()
