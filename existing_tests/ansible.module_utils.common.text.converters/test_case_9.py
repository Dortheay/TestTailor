import unittest
import timeout_decorator
import ansible.module_utils.common.text.converters as module_0

class Test_Converters_10(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        bool_0 = True
        var_0 = module_0.container_to_bytes(bool_0)

if __name__ == "__main__":
    unittest.main()
