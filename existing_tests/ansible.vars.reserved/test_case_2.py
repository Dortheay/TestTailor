import unittest
import timeout_decorator
import ansible.vars.reserved as module_0

class Test_Reserved_3(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_2(self):
        var_0 = module_0.get_reserved_names()
        float_0 = 0.5
        str_0 = '*a;n-,5H@\r-8r:/vH}\\'
        bool_0 = True
        str_1 = '|\rd8-7`H}'
        var_1 = module_0.warn_if_reserved(str_1)
        dict_0 = None
        tuple_0 = (float_0, str_0, bool_0, dict_0)
        str_2 = 'D'
        var_2 = module_0.warn_if_reserved(tuple_0, str_2)

if __name__ == "__main__":
    unittest.main()
