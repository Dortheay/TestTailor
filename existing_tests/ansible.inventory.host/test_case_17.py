import unittest
import timeout_decorator
import ansible.inventory.host as module_0
import ansible.inventory.group as module_1

class Test_Host_18(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_8(self):
        tuple_0 = None
        bytes_0 = b'\xaa]k'
        host_0 = module_0.Host(bytes_0)
        var_0 = host_0.set_variable(tuple_0, tuple_0)

if __name__ == "__main__":
    unittest.main()
