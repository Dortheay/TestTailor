import unittest
import timeout_decorator
import ansible.module_utils.common.text.formatters as module_0

class Test_Formatters_13(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_3(self):
        int_0 = 2642
        var_0 = module_0.bytes_to_human(int_0)

if __name__ == "__main__":
    unittest.main()
