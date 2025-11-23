import unittest
import timeout_decorator
import sanic.blueprint_group as module_0
import sanic.blueprints as module_1

class Test_Blueprint_group_5(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_4(self):
        int_0 = 1767
        str_0 = 'Sec-Websocket-Protocol'
        blueprint_0 = module_1.Blueprint(str_0)
        blueprint_group_0 = module_0.BlueprintGroup()
        blueprint_group_0.insert(int_0, blueprint_0)
        str_1 = "POiX2'I`KbDL<"
        blueprint_1 = module_1.Blueprint(str_1, str_1)
        blueprint_group_1 = module_0.BlueprintGroup()
        list_0 = [blueprint_1, str_1]
        var_0 = blueprint_1.exception(*list_0)
        blueprint_group_1.append(blueprint_1)
        var_1 = blueprint_group_1.middleware()
        int_1 = blueprint_group_0.__len__()

if __name__ == "__main__":
    unittest.main()
