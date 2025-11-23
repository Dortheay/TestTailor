import unittest
import timeout_decorator
import pymonet.monad_try as module_0

class Test_Monad_try_10(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_9(self):
        dict_0 = None
        int_0 = -3082
        set_0 = set()
        set_1 = {int_0}
        bool_0 = False
        try_0 = module_0.Try(set_1, bool_0)
        var_0 = try_0.get_or_else(set_0)
        int_1 = 268
        try_1 = module_0.Try(int_1, bool_0)
        str_0 = try_1.__str__()
        var_1 = try_1.bind(int_0)
        bool_1 = try_1.__eq__(str_0)
        bool_2 = True
        var_2 = try_1.filter(dict_0)
        try_2 = module_0.Try(try_0, bool_2)
        bool_3 = try_1.__eq__(bool_0)
        var_3 = try_1.get()
        var_4 = try_2.get_or_else(dict_0)

if __name__ == "__main__":
    unittest.main()
