import unittest
import timeout_decorator
import sanic.blueprint_group as module_0
import sanic.blueprints as module_1

class Test_Blueprint_group_3(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_2(self):
        blueprint_group_0 = module_0.BlueprintGroup()
        var_0 = blueprint_group_0.__iter__()
        var_1 = blueprint_group_0.middleware()
        blueprint_group_1 = module_0.BlueprintGroup()
        blueprint_group_2 = module_0.BlueprintGroup()
        bytes_0 = b'Kl\xd32\xa3G\xc6$\xb0\xb2B\xcc\x97\xe9u!\xc0\xe5'
        blueprint_group_3 = module_0.BlueprintGroup(bytes_0)

if __name__ == "__main__":
    unittest.main()
