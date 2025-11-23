import unittest
import timeout_decorator
import pymonet.monad_try as module_0

class Test_Monad_try_4(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_3(self):
        str_0 = '\n        :param semigroup: other semigroup to concat\n        :type semigroup: Max[B]\n        :returns: new Max with largest value\n        :rtype: Max[A | B]\n        '
        dict_0 = {}
        bool_0 = False
        try_0 = module_0.Try(dict_0, bool_0)
        var_0 = try_0.map(str_0)

if __name__ == "__main__":
    unittest.main()
