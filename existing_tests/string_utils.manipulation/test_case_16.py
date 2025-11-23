import unittest
import timeout_decorator
import string_utils.manipulation as module_0

class Test_Manipulation_17(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_5(self):
        try:
            str_0 = '-~~2NE4!2z!'
            str_1 = module_0.strip_html(str_0)
            str_2 = module_0.decompress(str_0, str_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
