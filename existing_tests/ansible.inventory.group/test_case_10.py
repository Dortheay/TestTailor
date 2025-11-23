import unittest
import timeout_decorator
import ansible.inventory.group as module_0

class Test_Group_11(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_10(self):
        group_0 = module_0.Group()
        var_0 = group_0.clear_hosts_cache()
        var_1 = group_0.clear_hosts_cache()
        tuple_0 = None
        var_2 = group_0.set_priority(tuple_0)

if __name__ == "__main__":
    unittest.main()
