import unittest
import timeout_decorator
import ansible.module_utils.common.parameters as module_0

class Test_Parameters_19(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_5(self):
        try:
            bytes_0 = b'z\x05\xfb\xf9\xfd%\xf2'
            dict_0 = {}
            var_0 = module_0.remove_values(bytes_0, dict_0)
            str_0 = ';4ka'
            var_1 = module_0.set_fallbacks(dict_0, str_0)
            var_2 = module_0.set_fallbacks(dict_0, bytes_0)
            var_3 = module_0.env_fallback(**dict_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
