import unittest
import timeout_decorator
import ansible.inventory.group as module_0

class Test_Group_1(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        group_0 = module_0.Group()

if __name__ == "__main__":
    unittest.main()
