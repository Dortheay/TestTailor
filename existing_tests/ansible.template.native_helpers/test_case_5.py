import unittest
import timeout_decorator
import ansible.template.native_helpers as module_0
import jinja2.runtime as module_1
import ansible.parsing.yaml.objects as module_2

class Test_Native_helpers_6(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        try:
            float_0 = 3679.372
            dict_0 = {float_0: float_0, float_0: float_0, float_0: float_0}
            list_0 = [dict_0]
            var_0 = module_0.ansible_native_concat(list_0)
            float_1 = -1739.811
            var_1 = module_0.ansible_native_concat(float_1)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
