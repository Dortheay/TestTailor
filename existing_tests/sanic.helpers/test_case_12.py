import unittest
import timeout_decorator
import sanic.helpers as module_0

class Test_Helpers_13(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_4(self):
        try:
            int_0 = None
            dict_0 = {int_0: int_0, int_0: int_0}
            var_0 = module_0.remove_entity_headers(dict_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
