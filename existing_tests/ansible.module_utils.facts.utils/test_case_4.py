import unittest
import timeout_decorator
import ansible.module_utils.facts.utils as module_0

class Test_Utils_5(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        bytes_0 = b'\xf1\xaf$'
        var_0 = module_0.get_mount_size(bytes_0)

if __name__ == "__main__":
    unittest.main()
