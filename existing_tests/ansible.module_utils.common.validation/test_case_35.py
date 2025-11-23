import unittest
import timeout_decorator
import ansible.module_utils.common.validation as module_0

class Test_Validation_36(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_35(self):
        try:
            float_0 = None
            int_0 = 860
            str_0 = '}O&S'
            bytes_0 = b'\x8a\xbd\xc4\xe5\xf9\xafX'
            list_0 = [bytes_0, str_0, float_0, int_0]
            tuple_0 = (list_0,)
            var_0 = module_0.check_required_one_of(tuple_0, list_0)
            bytes_1 = b'\xf5\xa1R\x8a6\x89A\x94o\xd2\xd8\xa7|J'
            bool_0 = False
            var_1 = module_0.check_required_one_of(bytes_1, bool_0, float_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
