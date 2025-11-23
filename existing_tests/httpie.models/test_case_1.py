import unittest
import timeout_decorator
import httpie.models as module_0

class Test_Models_2(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        try:
            int_0 = 2875
            str_0 = 'L3>\nkz/~db?'
            h_t_t_p_message_0 = module_0.HTTPMessage(str_0)
            iterable_0 = h_t_t_p_message_0.iter_lines(int_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
