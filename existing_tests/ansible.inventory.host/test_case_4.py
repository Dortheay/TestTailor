import unittest
import timeout_decorator
import ansible.inventory.host as module_0
import ansible.inventory.group as module_1

class Test_Host_5(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_4(self):
        try:
            bytes_0 = b'.'
            float_0 = 153.2
            host_0 = module_0.Host(float_0)
            var_0 = host_0.add_group(bytes_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
