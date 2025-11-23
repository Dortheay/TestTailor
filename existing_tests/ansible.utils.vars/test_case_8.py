import unittest
import timeout_decorator
import ansible.utils.vars as module_0

class Test_Vars_9(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_8(self):
        str_0 = 'valid_identifier'
        var_0 = module_0._isidentifier_PY3(str_0)
        str_1 = '_underscore'
        var_1 = module_0._isidentifier_PY3(str_1)
        str_2 = 'camelCase'
        var_2 = module_0._isidentifier_PY3(str_2)
        str_3 = 'snake_case'
        var_3 = module_0._isidentifier_PY3(str_3)
        str_4 = '123number'
        var_4 = module_0._isidentifier_PY3(str_4)
        str_5 = 'with space'
        var_5 = module_0._isidentifier_PY3(str_5)
        str_6 = 'special@chars'
        var_6 = module_0._isidentifier_PY3(str_6)
        str_7 = 'True'
        var_7 = module_0._isidentifier_PY3(str_7)
        str_8 = 'None'
        var_8 = module_0._isidentifier_PY3(str_8)
        str_9 = 'False'
        var_9 = module_0._isidentifier_PY3(str_9)
        str_10 = 'def'
        var_10 = module_0._isidentifier_PY3(str_10)
        str_11 = ''
        var_11 = module_0._isidentifier_PY3(str_11)
        int_0 = 123
        var_12 = module_0._isidentifier_PY3(int_0)
        str_12 = 'list'
        str_13 = [str_12]
        var_13 = module_0._isidentifier_PY3(str_13)

if __name__ == "__main__":
    unittest.main()
