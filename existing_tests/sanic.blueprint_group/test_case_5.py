import unittest
import timeout_decorator
import sanic.blueprint_group as module_0
import sanic.blueprints as module_1

class Test_Blueprint_group_6(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_5(self):
        str_0 = 'Gvw"q%dOL*D+OUd1K'
        blueprint_group_0 = module_0.BlueprintGroup(str_0)
        list_0 = [blueprint_group_0]
        var_0 = blueprint_group_0.middleware(*list_0)

if __name__ == "__main__":
    unittest.main()
