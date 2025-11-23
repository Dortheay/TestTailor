import unittest
import timeout_decorator
import ansible.inventory.host as module_0
import ansible.inventory.group as module_1

class Test_Host_11(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        host_0 = module_0.Host()
        var_0 = host_0.__str__()
        var_1 = host_0.__getstate__()

if __name__ == "__main__":
    unittest.main()
