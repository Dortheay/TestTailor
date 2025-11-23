import unittest
import timeout_decorator
import ansible.module_utils.common.text.converters as module_0

class Test_Converters_13(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_3(self):
        int_0 = -744
        var_0 = module_0.to_text(int_0)

if __name__ == "__main__":
    unittest.main()
