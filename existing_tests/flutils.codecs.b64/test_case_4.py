import unittest
import timeout_decorator
import flutils.codecs.b64 as module_0
import collections as module_1
import codecs as module_2

class Test_B64_5(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_3(self):
        try:
            module_0.register()
            int_0 = 3797
            str_0 = 'BxDadDu,r^sI\x0cmiFT\tUa'
            module_0.register()
            tuple_0 = module_0.encode(str_0)
            dict_0 = {str_0: str_0}
            tuple_1 = module_0.encode(str_0)
            user_string_0 = module_1.UserString(dict_0)
            tuple_2 = module_0.encode(user_string_0)
            tuple_3 = module_0.decode(int_0, user_string_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
