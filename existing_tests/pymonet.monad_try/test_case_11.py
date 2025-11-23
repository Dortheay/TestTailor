import unittest
import timeout_decorator
import pymonet.monad_try as module_0

class Test_Monad_try_12(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_11(self):
        str_0 = 'qCXmiB0ror\x0b$*\rk?{.'
        set_0 = {str_0, str_0, str_0, str_0}
        bool_0 = False
        tuple_0 = (bool_0,)
        try_0 = module_0.Try(tuple_0, bool_0)
        bool_1 = True
        int_0 = 609
        var_0 = try_0.bind(int_0)
        try_1 = module_0.Try(try_0, bool_1)
        var_1 = try_0.filter(tuple_0)
        var_2 = try_0.map(bool_1)
        str_1 = try_0.__str__()
        str_2 = 'oPWc,y}ZTIHHNv(b"'
        list_0 = [str_2, str_2]
        var_3 = try_1.get()
        bool_2 = False
        try_2 = module_0.Try(list_0, bool_2)
        float_0 = -202.0
        bool_3 = try_1.__eq__(try_1)
        var_4 = try_0.map(float_0)
        dict_0 = None
        var_5 = try_2.on_success(dict_0)
        bool_4 = try_0.__eq__(set_0)

if __name__ == "__main__":
    unittest.main()
