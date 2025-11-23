import unittest
import timeout_decorator
import youtube_dl.swfinterp as module_0

class Test_Swfinterp_3(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_2(self):
        try:
            bool_0 = True
            scope_dict_0 = module_0._ScopeDict(bool_0)
            var_0 = scope_dict_0.__repr__()
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
