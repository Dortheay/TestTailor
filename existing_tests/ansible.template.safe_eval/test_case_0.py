import unittest
import timeout_decorator
import ansible.template.safe_eval as module_0

class Test_Safe_eval_1(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        try:
            str_0 = 'r-/LM+4s\r~)'
            int_0 = 3803
            tuple_0 = ()
            var_0 = module_0.safe_eval(tuple_0)
            var_1 = module_0.safe_eval(str_0, str_0, int_0)
            bool_0 = False
            bytes_0 = b'\xedU\xa4.\x8bV\x13t)\xa7\x1f\xeb'
            var_2 = module_0.safe_eval(bool_0, bytes_0)
            bytes_1 = b'\x91\x10WN\xf7\xfd'
            str_1 = '}\x0c_]4'
            list_0 = [str_1]
            var_3 = module_0.safe_eval(bytes_1, list_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
