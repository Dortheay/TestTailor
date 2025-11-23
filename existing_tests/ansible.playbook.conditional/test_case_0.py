import unittest
import timeout_decorator
import ansible.playbook.conditional as module_0

class Test_Conditional_1(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        str_0 = '_/GDeWf$*h'
        bool_0 = True
        conditional_0 = module_0.Conditional(bool_0)
        var_0 = conditional_0.extract_defined_undefined(str_0)

if __name__ == "__main__":
    unittest.main()
