import unittest
import timeout_decorator
import httpie.models as module_0

class Test_Models_1(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        try:
            int_0 = -2226
            str_0 = 'json.indent:4'
            h_t_t_p_request_0 = module_0.HTTPRequest(str_0)
            tuple_0 = ()
            set_0 = {tuple_0, int_0, tuple_0, tuple_0}
            str_1 = 'x)o'
            h_t_t_p_request_1 = module_0.HTTPRequest(str_1)
            var_0 = h_t_t_p_request_1.iter_body(set_0)
            h_t_t_p_message_0 = module_0.HTTPMessage(tuple_0)
            iterable_0 = h_t_t_p_message_0.iter_body(int_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
