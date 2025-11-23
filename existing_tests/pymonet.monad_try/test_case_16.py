import unittest
import timeout_decorator
import pymonet.monad_try as module_0

class Test_Monad_try_17(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_4(self):
        try:
            bool_0 = True
            str_0 = 'Validation.fail[{}, {}]'
            bool_1 = True
            try_0 = module_0.Try(str_0, bool_1)
            bool_2 = try_0.__eq__(bool_0)
            str_1 = 'q_KXWb*\t'
            set_0 = set()
            bool_3 = False
            try_1 = module_0.Try(set_0, bool_3)
            var_0 = try_1.on_fail(str_1)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
