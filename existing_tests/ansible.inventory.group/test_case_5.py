import unittest
import timeout_decorator
import ansible.inventory.group as module_0

class Test_Group_6(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_5(self):
        group_0 = module_0.Group()
        dict_0 = {}
        var_0 = group_0.deserialize(dict_0)

if __name__ == "__main__":
    unittest.main()
