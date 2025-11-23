import unittest
import timeout_decorator
import ansible.module_utils.connection as module_0

class Test_Connection_2(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        try:
            str_0 = 'D&*t5Lh14b4\x0ctWP_8@!'
            str_1 = 'DIOAkr8"L!E \tg@)P'
            str_2 = 'Ra\n6@*\ts)DyK.wX))xl'
            dict_0 = {str_0: str_0, str_1: str_0, str_0: str_0, str_2: str_2}
            connection_error_0 = module_0.ConnectionError(str_1, **dict_0)
            int_0 = -1352
            float_0 = 566.7
            tuple_0 = (dict_0, connection_error_0, int_0, float_0)
            float_1 = -1354.7
            var_0 = module_0.send_data(tuple_0, float_1)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
