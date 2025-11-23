import unittest
import timeout_decorator
import flutes.structure as module_0

class Test_Structure_2(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        float_0 = 1.0
        var_0 = module_0.no_map_instance(float_0)
        bool_0 = None
        module_0.register_no_map_class(bool_0)
        list_0 = [bool_0, bool_0, bool_0, bool_0]
        var_1 = module_0.no_map_instance(list_0)

if __name__ == "__main__":
    unittest.main()
