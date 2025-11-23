import unittest
import timeout_decorator
import ansible.utils.vars as module_0

class Test_Vars_3(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_2(self):
        str_0 = '7c;fNdtY)FOPa)&9'
        var_0 = module_0.load_options_vars(str_0)

if __name__ == "__main__":
    unittest.main()
