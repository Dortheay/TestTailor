import unittest
import timeout_decorator
import youtube_dl.swfinterp as module_0

class Test_Swfinterp_7(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_6(self):
        try:
            bytes_0 = b'/\xba'
            multiname_0 = module_0._Multiname(bytes_0)
            var_0 = multiname_0.__repr__()
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
