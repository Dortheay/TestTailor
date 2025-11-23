import unittest
import timeout_decorator
import pytutils.lazy.lazy_regex as module_0

class Test_Lazy_regex_6(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_5(self):
        try:
            list_0 = []
            str_0 = 'dNsLrb2ZV1\x0bnw}o,Lua'
            var_0 = module_0.finditer_public(list_0, str_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
