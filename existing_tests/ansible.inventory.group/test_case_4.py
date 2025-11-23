import unittest
import timeout_decorator
import ansible.inventory.group as module_0

class Test_Group_5(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_4(self):
        group_0 = module_0.Group()
        var_0 = group_0.__getstate__()

if __name__ == "__main__":
    unittest.main()
