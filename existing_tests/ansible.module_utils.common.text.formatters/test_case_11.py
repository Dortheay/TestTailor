import unittest
import timeout_decorator
import ansible.module_utils.common.text.formatters as module_0

class Test_Formatters_12(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_2(self):
        int_0 = 148
        var_0 = module_0.human_to_bytes(int_0)

if __name__ == "__main__":
    unittest.main()
