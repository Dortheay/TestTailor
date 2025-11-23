import unittest
import timeout_decorator
import ansible.module_utils.common.validation as module_0

class Test_Validation_45(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_44(self):
        try:
            var_0 = None
            str_0 = ']e)1'
            str_1 = '72/DuLgm!ek"u'
            str_2 = 'value2'
            str_3 = {}
            str_4 = 'val1'
            str_5 = 'val2'
            str_6 = {str_0: str_4, str_1: str_4, str_2: str_5}
            str_7 = '3+\x0c4kU4R5rA}txh\t'
            var_1 = module_0.safe_eval(str_7)
            var_2 = module_0.check_required_by(str_3, str_6)
            str_8 = [str_1, str_2]
            str_9 = {str_0: str_8}
            var_3 = {str_0: str_5, str_1: var_0}
            var_4 = module_0.check_required_by(str_9, var_3)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
