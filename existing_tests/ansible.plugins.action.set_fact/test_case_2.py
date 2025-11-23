import unittest
import timeout_decorator
import ansible.plugins.action.set_fact as module_0

class Test_Set_fact_3(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_2(self):
        try:
            set_0 = set()
            str_0 = '>B\n\t\'HUYg\'c"{Ua@b`m'
            bool_0 = False
            list_0 = None
            bytes_0 = b'5\xfc]\xc5\x9afR\x03\xe8\xe2\x93o\xc8\x034\x84'
            float_0 = 100.0
            action_module_0 = module_0.ActionModule(set_0, str_0, bool_0, list_0, bytes_0, float_0)
            list_1 = None
            int_0 = 9
            bytes_1 = b'\xb5\x90\x01<M;\xf1\xd2\xc8\xa1\x17\xe7\xaf\x1d'
            tuple_0 = (list_1, int_0, bytes_1)
            set_1 = {bytes_1, bytes_1, list_1}
            bool_1 = False
            int_1 = 2275
            str_1 = 'W*gCZ2N4A\x0ckI*'
            bool_2 = False
            str_2 = 'TnoKVsy\nyS0@_'
            action_module_1 = module_0.ActionModule(int_1, str_1, int_1, bool_2, int_1, str_2)
            bool_3 = False
            str_3 = 'ba\r'
            dict_0 = {action_module_1: str_2, int_1: str_1}
            set_2 = set()
            action_module_2 = module_0.ActionModule(bool_1, action_module_1, bool_3, str_3, dict_0, set_2)
            var_0 = action_module_2.run(tuple_0, set_1)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
