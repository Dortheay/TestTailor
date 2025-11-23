import unittest
import timeout_decorator
import sanic.helpers as module_0

class Test_Helpers_3(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_2(self):
        float_0 = 796.6940871908391
        var_0 = module_0.has_message_body(float_0)

if __name__ == "__main__":
    unittest.main()
