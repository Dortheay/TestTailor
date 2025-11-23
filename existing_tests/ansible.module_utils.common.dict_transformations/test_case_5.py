import unittest
import timeout_decorator
import ansible.module_utils.common.dict_transformations as module_0

class Test_Dict_transformations_6(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_5(self):
        try:
            float_0 = None
            var_0 = module_0.recursive_diff(float_0, float_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
