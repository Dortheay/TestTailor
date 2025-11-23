import unittest
import timeout_decorator
import ansible.modules.subversion as module_0

class Test_Subversion_14(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_11(self):
        try:
            str_0 = ''
            set_0 = set()
            list_0 = [str_0, str_0, set_0, set_0]
            int_0 = -1981
            str_1 = '2?w2'
            int_1 = 10
            float_0 = -748.65
            str_2 = 'ansible.modules.subversion'
            str_3 = ',>?ko1H6J!.=&9(k6xnI'
            tuple_0 = (str_3,)
            tuple_1 = (tuple_0, tuple_0)
            str_4 = '^|'
            int_2 = -4045
            int_3 = 32600
            subversion_0 = module_0.Subversion(float_0, list_0, str_2, tuple_1, str_4, int_2, list_0, int_3)
            subversion_1 = module_0.Subversion(str_0, list_0, str_0, int_0, str_0, str_1, int_1, subversion_0)
            var_0 = subversion_1.revert()
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
