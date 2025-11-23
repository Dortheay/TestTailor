import unittest
import timeout_decorator
import ansible.template.native_helpers as module_0
import jinja2.runtime as module_1
import ansible.parsing.yaml.objects as module_2

class Test_Native_helpers_8(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_2(self):
        try:
            var_0 = []
            var_1 = module_0.ansible_native_concat(var_0)
            int_0 = 42
            int_1 = [int_0]
            var_2 = module_0.ansible_native_concat(int_1)
            str_0 = 'undefined'
            strict_undefined_0 = module_1.StrictUndefined(str_0)
            strict_undefined_1 = [strict_undefined_0]
            var_3 = module_0.ansible_native_concat(strict_undefined_1)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
