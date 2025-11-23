import unittest
import timeout_decorator
import ansible.module_utils.common.parameters as module_0

class Test_Parameters_20(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_6(self):
        try:
            bytes_0 = b'c=\xeb!\xa2\x83\xea\xe2&@\xdd\xc4'
            list_0 = [bytes_0, bytes_0, bytes_0]
            var_0 = module_0.remove_values(bytes_0, list_0)
            tuple_0 = ()
            dict_0 = {var_0: tuple_0, tuple_0: list_0}
            str_0 = None
            var_1 = module_0.set_fallbacks(dict_0, str_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
