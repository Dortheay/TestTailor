import unittest
import timeout_decorator
import ansible.module_utils.common.parameters as module_0

class Test_Parameters_7(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_6(self):
        str_0 = '@ RYY\\Ad5m&'
        str_1 = '\\='
        dict_0 = {str_0: str_0, str_1: str_1, str_1: str_1, str_1: str_0}
        list_0 = [dict_0, str_1]
        list_1 = [str_0]
        set_0 = set()
        var_0 = module_0.sanitize_keys(list_0, list_1, set_0)

if __name__ == "__main__":
    unittest.main()
