import unittest
import timeout_decorator
import ansible.module_utils.common.dict_transformations as module_0

class Test_Dict_transformations_14(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_2(self):
        str_0 = None
        int_0 = None
        var_0 = module_0.dict_merge(str_0, int_0)

if __name__ == "__main__":
    unittest.main()
