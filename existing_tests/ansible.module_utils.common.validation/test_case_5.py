import unittest
import timeout_decorator
import ansible.module_utils.common.validation as module_0

class Test_Validation_6(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_5(self):
        try:
            tuple_0 = ()
            dict_0 = {tuple_0: tuple_0, tuple_0: tuple_0, tuple_0: tuple_0}
            int_0 = -1188
            bool_0 = True
            tuple_1 = (dict_0, int_0, bool_0)
            dict_1 = {tuple_0: tuple_0, tuple_0: tuple_0, tuple_0: tuple_0, tuple_0: tuple_1}
            bytes_0 = b"u=\xd0\x0c\xc1\xce\x03\x92\x8a\xfc\x86bY\xe0'O\xf8"
            var_0 = module_0.check_missing_parameters(dict_1, bytes_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
