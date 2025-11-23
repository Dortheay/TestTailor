import unittest
import timeout_decorator
import ansible.module_utils.common.text.converters as module_0

class Test_Converters_11(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        set_0 = set()
        var_0 = module_0.to_bytes(set_0)

if __name__ == "__main__":
    unittest.main()
