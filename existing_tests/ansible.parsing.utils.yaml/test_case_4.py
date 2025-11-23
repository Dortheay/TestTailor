import unittest
import timeout_decorator
import ansible.parsing.utils.yaml as module_0

class Test_Yaml_5(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_4(self):
        try:
            str_0 = 'wD;|&'
            bool_0 = False
            int_0 = 1258
            dict_0 = {bool_0: bool_0, int_0: int_0, str_0: str_0}
            bytes_0 = None
            var_0 = module_0.from_yaml(str_0, bool_0, dict_0, bytes_0, dict_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
