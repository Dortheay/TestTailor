import unittest
import timeout_decorator
import ansible.inventory.host as module_0
import ansible.inventory.group as module_1

class Test_Host_14(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_4(self):
        bool_0 = True
        host_0 = module_0.Host(bool_0)
        var_0 = host_0.serialize()
        var_1 = host_0.serialize()

if __name__ == "__main__":
    unittest.main()
