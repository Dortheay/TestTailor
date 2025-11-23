import unittest
import timeout_decorator
import ansible.inventory.host as module_0
import ansible.inventory.group as module_1

class Test_Host_17(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_7(self):
        host_0 = module_0.Host()
        bytes_0 = b'\x99\xbf\xfay/'
        var_0 = host_0.remove_group(bytes_0)

if __name__ == "__main__":
    unittest.main()
