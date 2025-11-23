import unittest
import timeout_decorator
import sanic.blueprint_group as module_0
import sanic.blueprints as module_1

class Test_Blueprint_group_9(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_8(self):
        str_0 = 'Gvw"q%dOL*D+OUd1K'
        blueprint_group_0 = module_0.BlueprintGroup(str_0)
        str_1 = '!Zk|^Tt]"=E_X-'
        str_2 = 'q'
        dict_0 = {str_2: blueprint_group_0}
        var_0 = blueprint_group_0.middleware(**dict_0)
        blueprint_0 = module_1.Blueprint(str_0, str_1)
        blueprint_group_1 = module_0.BlueprintGroup()
        blueprint_group_1.append(blueprint_0)
        var_1 = blueprint_group_0.middleware(**dict_0)
        int_0 = blueprint_group_1.__len__()

if __name__ == "__main__":
    unittest.main()
