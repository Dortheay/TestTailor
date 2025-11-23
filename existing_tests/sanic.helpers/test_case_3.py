import unittest
import timeout_decorator
import sanic.helpers as module_0

class Test_Helpers_4(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_3(self):
        float_0 = 813.3321450168557
        var_0 = module_0.has_message_body(float_0)
        dict_0 = {}
        var_1 = module_0.remove_entity_headers(dict_0)

if __name__ == "__main__":
    unittest.main()
