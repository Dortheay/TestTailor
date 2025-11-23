import unittest
import timeout_decorator
import ansible.module_utils.splitter as module_0

class Test_Splitter_3(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        bytes_0 = b'\xc8'
        var_0 = module_0.unquote(bytes_0)

if __name__ == "__main__":
    unittest.main()
