import unittest
import timeout_decorator
import sanic.blueprint_group as module_0
import sanic.blueprints as module_1

class Test_Blueprint_group_7(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_6(self):
        str_0 = 'Gvw"q%dOL*D+OUd1K'
        blueprint_group_0 = module_0.BlueprintGroup(str_0)
        bytes_0 = None
        blueprint_0 = module_1.Blueprint(str_0, str_0, bytes_0)
        var_0 = blueprint_group_0.middleware()
        str_1 = '!PAr '
        bool_0 = True
        blueprint_1 = module_1.Blueprint(str_1, str_0, str_1, bool_0)
        blueprint_group_0.append(blueprint_1)
        list_0 = [bytes_0]
        var_1 = blueprint_group_0.middleware(*list_0)

if __name__ == "__main__":
    unittest.main()
