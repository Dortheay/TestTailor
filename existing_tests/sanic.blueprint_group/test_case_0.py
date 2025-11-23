import unittest
import timeout_decorator
import sanic.blueprint_group as module_0
import sanic.blueprints as module_1

class Test_Blueprint_group_1(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        blueprint_group_0 = module_0.BlueprintGroup()

if __name__ == "__main__":
    unittest.main()
