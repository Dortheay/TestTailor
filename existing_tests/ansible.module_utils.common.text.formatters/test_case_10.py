import unittest
import timeout_decorator
import ansible.module_utils.common.text.formatters as module_0

class Test_Formatters_11(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        bytes_0 = b'\xa4!\xf6'
        var_0 = module_0.lenient_lowercase(bytes_0)

if __name__ == "__main__":
    unittest.main()
