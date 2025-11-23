import unittest
import timeout_decorator
import ansible.cli.console as module_0

class Test_Console_21(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_10(self):
        try:
            dict_0 = None
            str_0 = 'i`l@c\t7aX\x0cq+Dq/n'
            console_c_l_i_0 = module_0.ConsoleCLI(str_0)
            var_0 = console_c_l_i_0.do_remote_user(dict_0)
            int_0 = 16
            bytes_0 = b'f'
            console_c_l_i_1 = module_0.ConsoleCLI(bytes_0)
            var_1 = console_c_l_i_1.post_process_args(int_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
