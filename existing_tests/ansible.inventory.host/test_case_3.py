import unittest
import timeout_decorator
import ansible.inventory.host as module_0
import ansible.inventory.group as module_1

class Test_Host_4(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_3(self):
        try:
            host_0 = module_0.Host()
            var_0 = host_0.populate_ancestors()
            var_1 = host_0.get_vars()
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
