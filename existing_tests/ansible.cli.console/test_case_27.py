import unittest
import timeout_decorator
import ansible.cli.console as module_0

class Test_Console_28(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_17(self):
        try:
            bytes_0 = b'i/\xa4\xe0\x0c\xbb;b\xa4'
            float_0 = None
            str_0 = 'notice'
            bytes_1 = b'\xad\xc1\xc3\x13\x04\xd4\x94'
            str_1 = '`'
            console_c_l_i_0 = module_0.ConsoleCLI(str_1)
            var_0 = console_c_l_i_0.completedefault(bytes_0, float_0, str_0, bytes_1)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
