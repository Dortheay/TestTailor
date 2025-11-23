import unittest
import timeout_decorator
import mimesis.schema as module_0

class Test_Schema_9(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_6(self):
        try:
            abstract_field_0 = module_0.AbstractField()
            str_0 = "GH4.D=''85,t{hv"
            any_0 = abstract_field_0.__call__(str_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
