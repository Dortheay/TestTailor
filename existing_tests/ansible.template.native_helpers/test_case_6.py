import unittest
import timeout_decorator
import ansible.template.native_helpers as module_0
import jinja2.runtime as module_1
import ansible.parsing.yaml.objects as module_2

class Test_Native_helpers_7(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        try:
            int_0 = -1834
            list_0 = [int_0]
            list_1 = [int_0, int_0, list_0, list_0]
            str_0 = '.9R!"&'
            var_0 = module_0.ansible_native_concat(str_0)
            tuple_0 = ()
            var_1 = module_0.ansible_native_concat(tuple_0)
            bytes_0 = b')\xfc~\xae\xdeH\x9e}\xeb\x93\\'
            set_0 = {bytes_0, int_0, int_0, bytes_0}
            var_2 = module_0.ansible_native_concat(bytes_0)
            var_3 = module_0.ansible_native_concat(set_0)
            var_4 = module_0.ansible_native_concat(list_1)
            var_5 = module_0.ansible_native_concat(str_0)
            float_0 = 1246.30265
            var_6 = module_0.ansible_native_concat(float_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
