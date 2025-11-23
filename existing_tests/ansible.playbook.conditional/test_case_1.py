import unittest
import timeout_decorator
import ansible.playbook.conditional as module_0

class Test_Conditional_2(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        var_0 = object()
        conditional_0 = module_0.Conditional(var_0)
        str_0 = "hostvars['myhost'] is defined and some_var is not defined"
        var_1 = conditional_0.extract_defined_undefined(str_0)

if __name__ == "__main__":
    unittest.main()
