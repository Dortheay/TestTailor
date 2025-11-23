import unittest
import timeout_decorator
import youtube_dl.swfinterp as module_0

class Test_Swfinterp_5(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_4(self):
        try:
            str_0 = "S\t|>) T7dY'OMM6"
            int_0 = 124
            dict_0 = {}
            undefined_0 = module_0._Undefined(**dict_0)
            var_0 = undefined_0.__bool__()
            list_0 = [int_0]
            a_v_m_class_0 = module_0._AVMClass(str_0, int_0, list_0)
            var_1 = a_v_m_class_0.register_methods(dict_0)
            scope_dict_0 = None
            scope_dict_1 = module_0._ScopeDict(scope_dict_0)
            bytes_0 = b'\x99\xe5\xf64\x14r'
            scope_dict_2 = module_0._ScopeDict(bytes_0)
            var_2 = scope_dict_2.__repr__()
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
