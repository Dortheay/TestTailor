import unittest
import timeout_decorator
import ansible.inventory.group as module_0

class Test_Group_24(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_4(self):
        try:
            group_0 = module_0.Group()
            var_0 = group_0.__str__()
            var_1 = group_0.get_hosts()
            str_0 = 'uc"\na=+J|VfT{H'
            var_2 = group_0.__str__()
            var_3 = group_0.remove_host(str_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
