import unittest
import timeout_decorator
import flutes.structure as module_0

class Test_Structure_17(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_12(self):
        try:
            dict_0 = {}
            int_0 = 512
            var_0 = module_0.map_structure(int_0, dict_0)
            bool_0 = True
            int_1 = 512
            tuple_0 = (bool_0,)
            var_1 = module_0.map_structure_zip(int_1, tuple_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
