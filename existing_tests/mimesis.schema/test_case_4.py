import unittest
import timeout_decorator
import mimesis.schema as module_0

class Test_Schema_5(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_2(self):
        try:
            callable_0 = None
            schema_0 = module_0.Schema(callable_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
