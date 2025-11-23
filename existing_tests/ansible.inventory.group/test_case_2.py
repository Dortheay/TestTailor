import unittest
import timeout_decorator
import ansible.inventory.group as module_0

class Test_Group_3(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_2(self):
        group_0 = module_0.Group()
        var_0 = group_0.__getstate__()
        var_1 = group_0.__repr__()

if __name__ == "__main__":
    unittest.main()
