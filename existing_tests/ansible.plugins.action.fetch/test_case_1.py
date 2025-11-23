import unittest
import timeout_decorator
import ansible.plugins.action.fetch as module_0

class Test_Fetch_2(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        try:
            str_0 = '\n[bI_GA5!uC8>/xb;{N'
            tuple_0 = (str_0,)
            str_1 = 'f\x0c\n+>W_$R0qP56|B$e \r'
            bool_0 = False
            float_0 = -561.822
            bytes_0 = b'\xe8:lT,\x94\xa9\x8d\x04 \xcb\xed\x08'
            str_2 = 'real:used'
            list_0 = []
            dict_0 = {}
            str_3 = '+j(+WekB,-SEu;+#gK'
            int_0 = 4095
            bytes_1 = b'\x01,\x84-l\xbbp8*g'
            int_1 = 2077
            int_2 = 16
            str_4 = 'kAc7Uq8*\n5zG(cs~\x0c'
            bytes_2 = b'y\xb3\xdc'
            action_module_0 = module_0.ActionModule(float_0, int_2, str_4, dict_0, str_2, bytes_2)
            float_1 = None
            action_module_1 = module_0.ActionModule(tuple_0, int_1, action_module_0, dict_0, float_1, action_module_0)
            set_0 = {str_3, str_4}
            action_module_2 = module_0.ActionModule(int_0, bytes_1, action_module_1, set_0, dict_0, list_0)
            action_module_3 = module_0.ActionModule(dict_0, list_0, str_3, float_1, action_module_2, dict_0)
            action_module_4 = module_0.ActionModule(tuple_0, str_2, list_0, dict_0, bool_0, action_module_3)
            float_2 = 2096.72
            tuple_1 = (float_2,)
            tuple_2 = (float_0, bytes_0, tuple_1)
            dict_1 = {str_1: str_1, bool_0: tuple_2, bool_0: tuple_2}
            str_5 = 'g[R\x0b\r}PK5\nq5N'
            str_6 = '\\346&3'
            bytes_3 = b'!\xc8\x0e\xeeJ\x80\xb0\xdf\x104?\x94\xcb\xa0#\x99\xac'
            action_module_5 = module_0.ActionModule(str_5, str_1, dict_1, dict_0, str_6, bytes_3)
            str_7 = '@\rVGs\tDN$@{B/&rK=X\\R'
            action_module_6 = module_0.ActionModule(tuple_2, int_2, bool_0, dict_1, set_0, bool_0)
            var_0 = action_module_6.run(str_7, dict_1)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
