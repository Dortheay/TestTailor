import unittest
import timeout_decorator
import flutes.structure as module_0

class Test_Structure_7(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_2(self):
        try:
            int_0 = -481
            var_0 = module_0.no_map_instance(int_0)
            str_0 = 'uA(XUx[1fBF0y'
            dict_0 = {str_0: var_0}
            var_1 = module_0.map_structure(str_0, dict_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
