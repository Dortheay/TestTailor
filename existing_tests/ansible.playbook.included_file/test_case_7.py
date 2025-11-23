import unittest
import timeout_decorator
import ansible.playbook.included_file as module_0

class Test_Included_file_8(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_5(self):
        try:
            str_0 = 'X-vg~ Q+}4g'
            list_0 = [str_0, str_0]
            str_1 = '/P}0/"*+XJ]^F'
            str_2 = 'TI9PA<qo&vmU'
            str_3 = 'pn4vt<EQJ{y2J_X6'
            bytes_0 = b''
            bool_0 = False
            int_0 = -283
            included_file_0 = module_0.IncludedFile(str_2, str_3, bytes_0, bool_0, int_0)
            included_file_1 = module_0.IncludedFile(list_0, str_1, list_0, included_file_0, int_0)
            str_4 = 'E:~27\x0bsBdvr'
            included_file_2 = module_0.IncludedFile(included_file_1, str_4, list_0, bytes_0)
            var_0 = included_file_0.__repr__()
            var_1 = included_file_1.__eq__(included_file_1)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
