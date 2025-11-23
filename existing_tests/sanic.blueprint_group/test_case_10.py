import unittest
import timeout_decorator
import sanic.blueprint_group as module_0

class Test_Blueprint_group_11(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        try:
            complex_0 = None
            bool_0 = True
            dict_0 = {complex_0: complex_0, complex_0: complex_0, bool_0: complex_0}
            list_0 = []
            blueprint_group_0 = module_0.BlueprintGroup(list_0)
            var_0 = blueprint_group_0.__getitem__(dict_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
