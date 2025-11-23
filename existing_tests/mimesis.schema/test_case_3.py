import unittest
import timeout_decorator
import mimesis.schema as module_0

class Test_Schema_4(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        try:
            abstract_field_0 = module_0.AbstractField()
            any_0 = abstract_field_0.__call__()
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
