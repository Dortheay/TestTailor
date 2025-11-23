import unittest
import timeout_decorator
import ansible.module_utils.connection as module_0

class Test_Connection_5(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_4(self):
        try:
            str_0 = '8J8G^,Q%C/nJr_p'
            str_1 = "L;+>'\x0b2l;9KQ&xHG%u3Y"
            float_0 = None
            int_0 = 911
            tuple_0 = (str_1, float_0, int_0)
            var_0 = module_0.request_builder(tuple_0)
            bool_0 = False
            var_1 = module_0.exec_command(str_0, bool_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
