import unittest
import timeout_decorator
import sanic.blueprint_group as module_0
import sanic.blueprints as module_1

class Test_Blueprint_group_10(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_9(self):
        blueprint_group_0 = module_0.BlueprintGroup()
        var_0 = blueprint_group_0.middleware()
        str_0 = 't^%}i4X@qD'
        float_0 = 881.8565
        blueprint_0 = module_1.Blueprint(str_0, str_0, float_0)
        float_1 = -2021.46487
        list_0 = [var_0, blueprint_0, blueprint_group_0, float_1]
        dict_0 = {str_0: list_0, str_0: list_0}
        var_1 = blueprint_group_0.middleware(*list_0, **dict_0)

if __name__ == "__main__":
    unittest.main()
