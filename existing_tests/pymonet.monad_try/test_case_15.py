import unittest
import timeout_decorator
import pymonet.monad_try as module_0

class Test_Monad_try_16(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_3(self):
        try:
            str_0 = "}5'7"
            set_0 = {str_0}
            bool_0 = True
            try_0 = module_0.Try(set_0, bool_0)
            str_1 = try_0.__str__()
            bytes_0 = b'\xa9\xc7\xee\xccy$F6\xed\xc6ufW{W\xb4d\x1eD\x82'
            bool_1 = True
            try_1 = module_0.Try(bytes_0, bool_1)
            var_0 = try_1.on_success(str_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
