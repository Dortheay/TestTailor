import unittest
import timeout_decorator
import ansible.plugins.action.copy as module_0

class Test_Copy_1(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        try:
            tuple_0 = ()
            str_0 = 'R<T'
            set_0 = {tuple_0, tuple_0, tuple_0, str_0}
            str_1 = '#BH<H['
            float_0 = -306.588904
            list_0 = [str_0, str_1, tuple_0, str_1]
            str_2 = '3[p:s'
            action_module_0 = module_0.ActionModule(set_0, str_1, float_0, list_0, str_2, list_0)
            var_0 = action_module_0.run()
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
