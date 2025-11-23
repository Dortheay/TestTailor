import unittest
import timeout_decorator
import ansible.module_utils.common.validation as module_0

class Test_Validation_32(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_31(self):
        try:
            str_0 = 'statically_loaded'
            str_1 = 'q'
            set_0 = set()
            tuple_0 = (str_0, str_0, str_1, set_0)
            str_2 = '?]<AhwUN=\nXmt^yHL'
            var_0 = module_0.count_terms(tuple_0, str_2)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
