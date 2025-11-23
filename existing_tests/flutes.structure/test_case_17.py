import unittest
import timeout_decorator
import flutes.structure as module_0

class Test_Structure_18(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_13(self):
        try:
            str_0 = 'jL4Ft)*'
            module_0.register_no_map_class(str_0)
            var_0 = module_0.no_map_instance(str_0)
            dict_0 = {str_0: var_0}
            set_0 = set()
            var_1 = module_0.map_structure(dict_0, set_0)
            dict_1 = {}
            list_0 = module_0.reverse_map(dict_1)
            int_0 = -1047
            float_0 = 1865.2
            tuple_0 = (list_0, float_0)
            list_1 = module_0.reverse_map(dict_1)
            var_2 = module_0.map_structure(int_0, tuple_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
