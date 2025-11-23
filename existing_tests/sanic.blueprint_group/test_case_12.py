import unittest
import timeout_decorator
import sanic.blueprint_group as module_0

class Test_Blueprint_group_13(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_2(self):
        try:
            dict_0 = {}
            bool_0 = False
            list_0 = [dict_0, bool_0, bool_0]
            int_0 = 2382
            blueprint_group_0 = module_0.BlueprintGroup(int_0)
            blueprint_group_0.__delitem__(list_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
