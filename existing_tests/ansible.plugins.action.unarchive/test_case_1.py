import unittest
import timeout_decorator
import ansible.plugins.action.unarchive as module_0

class Test_Unarchive_2(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        try:
            tuple_0 = None
            set_0 = None
            float_0 = 428.8463
            int_0 = -1060
            bytes_0 = b'K'
            bool_0 = True
            dict_0 = {bytes_0: bool_0, bool_0: int_0, float_0: set_0}
            list_0 = []
            bytes_1 = b'"L(\xf7*\x0ef;\x80\xd7q\xeb\xb7'
            str_0 = '@Y9_'
            bytes_2 = b"\xdfL'\xc1N#\xc5\xe1\xe9\x1c?5\xe1\xff"
            action_module_0 = module_0.ActionModule(list_0, bytes_1, bool_0, str_0, bytes_2, tuple_0)
            var_0 = action_module_0.run(dict_0, int_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
