import unittest
import timeout_decorator
import sanic.helpers as module_0

class Test_Helpers_2(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        int_0 = -2942
        var_0 = module_0.has_message_body(int_0)

if __name__ == "__main__":
    unittest.main()
