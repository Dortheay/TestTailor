import unittest
import timeout_decorator
import pymonet.monad_try as module_0

class Test_Monad_try_15(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_2(self):
        try:
            bytes_0 = b'\x87\xcb\n\x03(\x9d`'
            str_0 = 'vWK##^! j\x0b$g-2UWs%VW'
            bool_0 = False
            try_0 = module_0.Try(str_0, bool_0)
            float_0 = 585.040817
            list_0 = None
            int_0 = -1407
            tuple_0 = (float_0, list_0, int_0)
            bool_1 = False
            try_1 = module_0.Try(tuple_0, bool_1)
            var_0 = try_1.on_success(try_0)
            set_0 = {bytes_0, bytes_0, bytes_0, bytes_0}
            str_1 = 'hS$aB3*0EvY\x0c3?;'
            tuple_1 = (bytes_0, set_0, set_0, str_1)
            list_1 = [tuple_1, bytes_0, str_1, bytes_0]
            str_2 = 'ImmutableList[T]'
            dict_0 = {str_2: str_2, str_2: str_2, str_2: str_2}
            bool_2 = True
            try_2 = module_0.Try(dict_0, bool_2)
            var_1 = try_2.map(list_1)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
