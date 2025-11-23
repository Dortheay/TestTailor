import unittest
import timeout_decorator
import ansible.module_utils.common.text.converters as module_0

class Test_Converters_16(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_6(self):
        str_0 = 'N'
        var_0 = module_0.container_to_text(str_0)

if __name__ == "__main__":
    unittest.main()
