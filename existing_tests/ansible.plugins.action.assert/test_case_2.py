import unittest
import timeout_decorator
import ansible.plugins.action.assert as module_0

class Test_Assert_3(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        try:
            bytes_0 = b'\x18\x0b\xd2\x19\x11\xad\x1d8\xd5\xdf&3\xc2\xf5\x7f'
            set_0 = {bytes_0, bytes_0, bytes_0}
            bytes_1 = b'\xdc\xe2\x80\xddRyH\t'
            set_1 = set()
            float_0 = 0.2
            list_0 = []
            dict_0 = None
            action_module_0 = module_0.ActionModule(bytes_1, set_0, set_1, float_0, list_0, dict_0)
            str_0 = None
            bool_0 = False
            str_1 = 'S<}Ch]\nF:'
            str_2 = '\ts Ch|t'
            dict_1 = {bool_0: str_2, str_2: str_1}
            int_0 = -470
            action_module_1 = module_0.ActionModule(bool_0, str_1, str_2, dict_1, int_0, bytes_0)
            var_0 = action_module_1.run(str_0, set_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
