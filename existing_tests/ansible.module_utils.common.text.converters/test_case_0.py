import unittest
import timeout_decorator
import ansible.module_utils.common.text.converters as module_0

class Test_Converters_1(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        try:
            bool_0 = True
            dict_0 = {}
            var_0 = module_0.to_bytes(bool_0, dict_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
