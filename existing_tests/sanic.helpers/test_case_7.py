import unittest
import timeout_decorator
import sanic.helpers as module_0

class Test_Helpers_8(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_7(self):
        int_0 = 100
        var_0 = module_0.has_message_body(int_0)
        int_1 = 204
        var_1 = module_0.has_message_body(int_1)
        int_2 = 304
        var_2 = module_0.has_message_body(int_2)
        int_3 = 200
        var_3 = module_0.has_message_body(int_3)
        int_4 = 201
        var_4 = module_0.has_message_body(int_4)
        int_5 = 400
        var_5 = module_0.has_message_body(int_5)
        int_6 = 500
        var_6 = module_0.has_message_body(int_6)

if __name__ == "__main__":
    unittest.main()
