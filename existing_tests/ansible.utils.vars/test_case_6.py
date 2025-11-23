import unittest
import timeout_decorator
import ansible.utils.vars as module_0

class Test_Vars_7(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_6(self):
        var_0 = module_0.get_unique_id()
        str_0 = 'hFwPbV'
        var_1 = module_0._isidentifier_PY3(str_0)
        var_2 = module_0.load_options_vars(str_0)
        str_1 = 'tsDYOKZ'
        var_3 = module_0.load_extra_vars(str_1)

if __name__ == "__main__":
    unittest.main()
