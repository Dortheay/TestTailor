import unittest
import timeout_decorator
import ansible.module_utils.common.text.formatters as module_0

class Test_Formatters_4(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_3(self):
        try:
            str_0 = '/aNpFW\tl*&\x0b'
            var_0 = module_0.bytes_to_human(str_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
