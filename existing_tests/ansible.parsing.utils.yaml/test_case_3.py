import unittest
import timeout_decorator
import ansible.parsing.utils.yaml as module_0

class Test_Yaml_4(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_3(self):
        try:
            int_0 = 4089
            str_0 = '~?/<UP{BX[UUJV7'
            bytes_0 = b'y\x0e8\xacR\xef\x80'
            list_0 = [int_0, int_0, bytes_0]
            bool_0 = False
            var_0 = module_0.from_yaml(str_0, list_0, bool_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
