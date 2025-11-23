import unittest
import timeout_decorator
import mimesis.schema as module_0

class Test_Schema_3(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        try:
            str_0 = 'c['
            abstract_field_0 = module_0.AbstractField()
            any_0 = abstract_field_0.__call__(str_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
