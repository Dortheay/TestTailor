import unittest
import timeout_decorator
import flutes.structure as module_0

class Test_Structure_8(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_3(self):
        try:
            dict_0 = {}
            list_0 = module_0.reverse_map(dict_0)
            int_0 = -1047
            float_0 = 1864.5681548291518
            tuple_0 = (list_0, float_0)
            list_1 = module_0.reverse_map(dict_0)
            var_0 = module_0.map_structure(int_0, tuple_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
