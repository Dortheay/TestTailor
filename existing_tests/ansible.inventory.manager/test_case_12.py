import unittest
import timeout_decorator
import ansible.inventory.manager as module_0

class Test_Manager_13(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        bytes_0 = b'\xda\xfd\xf5\x14\xa7\x9d\xaal\x00\xf1`'
        var_0 = module_0.split_host_pattern(bytes_0)

if __name__ == "__main__":
    unittest.main()
