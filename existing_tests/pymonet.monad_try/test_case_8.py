import unittest
import timeout_decorator
import pymonet.monad_try as module_0

class Test_Monad_try_9(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_8(self):
        dict_0 = {}
        tuple_0 = (dict_0,)
        int_0 = 819
        list_0 = [tuple_0, int_0]
        bytes_0 = b''
        list_1 = [bytes_0, bytes_0]
        float_0 = 8.4256
        list_2 = [float_0, list_1]
        tuple_1 = (bytes_0, list_1, list_2)
        bool_0 = False
        try_0 = module_0.Try(tuple_1, bool_0)
        try_1 = module_0.Try(try_0, bool_0)
        var_0 = try_1.get_or_else(list_0)

if __name__ == "__main__":
    unittest.main()
