import unittest
import timeout_decorator
import youtube_dl.swfinterp as module_0

class Test_Swfinterp_12(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        str_0 = 'N'
        multiname_0 = module_0._Multiname(str_0)
        undefined_0 = module_0._Undefined()
        var_0 = undefined_0.__hash__()
        undefined_1 = module_0._Undefined()
        var_1 = undefined_1.__hash__()
        var_2 = undefined_1.__str__()

if __name__ == "__main__":
    unittest.main()
