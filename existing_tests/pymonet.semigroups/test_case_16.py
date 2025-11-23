import unittest
import timeout_decorator
import pymonet.semigroups as module_0

class Test_Semigroups_17(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_5(self):
        try:
            int_0 = -14
            bytes_0 = b'{\x8a\x94\xa6\x9e\x9c\x80\xb8\xadNM\xb1\x86'
            last_0 = module_0.Last(bytes_0)
            max_0 = module_0.Max(last_0)
            var_0 = max_0.concat(int_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
