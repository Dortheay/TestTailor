import unittest
import timeout_decorator
import pymonet.monad_try as module_0

class Test_Monad_try_6(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_5(self):
        str_0 = 'ztJ5S\x0bw[W+'
        str_1 = '5iJGvG6m4i/A>"S4}S'
        bool_0 = True
        try_0 = module_0.Try(str_1, bool_0)
        var_0 = try_0.on_fail(str_0)

if __name__ == "__main__":
    unittest.main()
