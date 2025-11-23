import unittest
import timeout_decorator
import ansible.utils.vars as module_0

class Test_Vars_5(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_4(self):
        str_0 = '.|)/3Cb'
        dict_0 = {}
        var_0 = module_0.load_options_vars(dict_0)
        var_1 = module_0._isidentifier_PY3(str_0)
        var_2 = module_0.get_unique_id()

if __name__ == "__main__":
    unittest.main()
