import unittest
import timeout_decorator
import sanic.helpers as module_0

class Test_Helpers_9(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        try:
            complex_0 = None
            var_0 = module_0.remove_entity_headers(complex_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
