import unittest
import timeout_decorator
import ansible.utils.vars as module_0

class Test_Vars_14(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_3(self):
        try:
            float_0 = 1.5
            list_0 = [float_0, float_0]
            var_0 = module_0.merge_hash(float_0, list_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
