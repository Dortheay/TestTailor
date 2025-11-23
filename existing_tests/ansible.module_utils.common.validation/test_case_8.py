import unittest
import timeout_decorator
import ansible.module_utils.common.validation as module_0

class Test_Validation_9(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_8(self):
        try:
            str_0 = '|:Y1Y|a(mxwodj2aR'
            str_1 = 'ggs|Ub#cGnk^\x0c\\YO'
            list_0 = [str_0]
            var_0 = module_0.check_type_str(str_1, list_0)
            var_1 = module_0.safe_eval(str_0)
            list_1 = [str_0, str_0]
            var_2 = module_0.check_type_dict(list_1)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
