import unittest
import timeout_decorator
import ansible.module_utils.common.text.formatters as module_0

class Test_Formatters_9(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_8(self):
        try:
            str_0 = '1K'
            var_0 = module_0.human_to_bytes(str_0)
            str_1 = '1M'
            var_1 = module_0.human_to_bytes(str_1)
            str_2 = '1G'
            var_2 = module_0.human_to_bytes(str_2)
            str_3 = '1T'
            var_3 = module_0.human_to_bytes(str_3)
            str_4 = '1P'
            var_4 = module_0.human_to_bytes(str_4)
            str_5 = '1E'
            var_5 = module_0.human_to_bytes(str_5)
            str_6 = '1Z'
            var_6 = module_0.human_to_bytes(str_6)
            str_7 = '1Y'
            var_7 = module_0.human_to_bytes(str_7)
            str_8 = '1'
            str_9 = 'K'
            var_8 = module_0.human_to_bytes(str_8, str_9)
            str_10 = '2M'
            var_9 = module_0.human_to_bytes(str_10)
            str_11 = '0.5K'
            var_10 = module_0.human_to_bytes(str_11)
            str_12 = '1KB'
            var_11 = module_0.human_to_bytes(str_12)
            int_0 = 24
            str_13 = 'M'
            var_12 = module_0.human_to_bytes(int_0, str_13)
            str_14 = '1Mb'
            bool_0 = True
            var_13 = module_0.human_to_bytes(str_14, bool_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
