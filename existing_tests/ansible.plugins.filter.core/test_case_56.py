import unittest
import timeout_decorator
import ansible.plugins.filter.core as module_0

class Test_Core_57(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_7(self):
        bytes_0 = b'y`^\x9c\xce\xb2C\x98\xc4H_#\x9aM\x19'
        var_0 = module_0.fileglob(bytes_0)

if __name__ == "__main__":
    unittest.main()
