import unittest
import timeout_decorator
import sanic.blueprint_group as module_0
import sanic.blueprints as module_1

class Test_Blueprint_group_2(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        str_0 = 'Gvw"q%dOL*D+OUd1K'
        blueprint_group_0 = module_0.BlueprintGroup(str_0)
        str_1 = '!Zk|^Tt]"=E_X-'
        blueprint_0 = module_1.Blueprint(str_1)
        blueprint_group_0.append(blueprint_0)
        var_0 = blueprint_group_0.middleware()

if __name__ == "__main__":
    unittest.main()
