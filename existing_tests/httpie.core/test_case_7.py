import unittest
import timeout_decorator
import argparse as module_0
import requests.models as module_1
import httpie.core as module_2
import httpie.context as module_3

class Test_Core_8(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_3(self):
        try:
            environment_0 = module_3.Environment()
            var_0 = module_2.print_debug_info(environment_0)
            exit_status_0 = module_2.main()
            str_0 = 'X}RL_7kD['
            str_1 = '/-r\rGf|.~G'
            var_1 = environment_0.log_error(str_1)
            list_0 = [str_0]
            var_2 = module_2.print_debug_info(environment_0)
            str_2 = 'o]&xn[K'
            list_1 = module_2.decode_raw_args(list_0, str_2)
            exit_status_1 = module_2.main()
            dict_0 = {str_1: environment_0, str_2: exit_status_0}
            exit_status_2 = module_2.main(dict_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
