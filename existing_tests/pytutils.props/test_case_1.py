import unittest
import timeout_decorator
import pytutils.props as module_0

class Test_Props_2(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        try:
            bool_0 = False
            list_0 = [bool_0]
            bytes_0 = b'\xf3\x1cd\x8aj[\xc0\x00\x02\xb5.'
            setterproperty_0 = module_0.setterproperty(bytes_0)
            var_0 = setterproperty_0.__set__(bool_0, list_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
