import unittest
import timeout_decorator
import flutes.structure as module_0

class Test_Structure_4(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_3(self):
        tuple_0 = ()
        str_0 = 'OkoiLS|2~:'
        list_0 = [tuple_0]
        var_0 = module_0.map_structure_zip(str_0, list_0)
        var_1 = module_0.no_map_instance(tuple_0)
        set_0 = {var_1, tuple_0, tuple_0, var_1}
        var_2 = module_0.no_map_instance(set_0)
        dict_0 = None
        float_0 = 0.1
        list_1 = [dict_0, var_1, float_0, tuple_0]
        var_3 = module_0.map_structure(list_1, tuple_0)
        dict_1 = {}
        list_2 = module_0.reverse_map(dict_1)

if __name__ == "__main__":
    unittest.main()
