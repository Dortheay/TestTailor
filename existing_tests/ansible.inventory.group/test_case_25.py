import unittest
import timeout_decorator
import ansible.inventory.group as module_0

class Test_Group_26(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_6(self):
        try:
            group_0 = module_0.Group()
            var_0 = group_0.get_hosts()
            bool_0 = True
            var_1 = group_0.get_hosts()
            var_2 = group_0.__setstate__(bool_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
