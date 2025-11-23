import unittest
import timeout_decorator
import flutes.structure as module_0

class Test_Structure_10(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_5(self):
        try:
            type_0 = None
            type_1 = None
            module_0.register_no_map_class(type_1)
            module_0.register_no_map_class(type_1)
            module_0.register_no_map_class(type_0)
            tuple_0 = None
            dict_0 = {tuple_0: tuple_0}
            int_0 = 1163
            list_0 = [dict_0, int_0, tuple_0, tuple_0]
            list_1 = [int_0, list_0]
            str_0 = '1D-b"a,(|wo'
            str_1 = '0p'
            list_2 = [dict_0, list_1, str_0, str_1]
            var_0 = module_0.map_structure(tuple_0, list_2)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
