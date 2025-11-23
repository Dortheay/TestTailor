import unittest
import timeout_decorator
import ansible.module_utils.common.text.formatters as module_0

class Test_Formatters_8(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_7(self):
        try:
            str_0 = '2K'
            var_0 = module_0.human_to_bytes(str_0)
            str_1 = '10M'
            var_1 = module_0.human_to_bytes(str_1)
            str_2 = '1G'
            var_2 = module_0.human_to_bytes(str_2)
            str_3 = '1.5T'
            var_3 = module_0.human_to_bytes(str_3)
            str_4 = '100'
            str_5 = 'M'
            var_4 = module_0.human_to_bytes(str_4, str_5)
            str_6 = '1B'
            var_5 = module_0.human_to_bytes(str_6)
            str_7 = '1Kb'
            bool_0 = True
            var_6 = module_0.human_to_bytes(str_7, bool_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
