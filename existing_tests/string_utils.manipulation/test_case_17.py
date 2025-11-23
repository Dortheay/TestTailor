import unittest
import timeout_decorator
import string_utils.manipulation as module_0

class Test_Manipulation_18(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_6(self):
        try:
            str_0 = 'This is a string that will be compressed and then decompressed.'
            str_1 = module_0.compress(str_0)
            str_2 = module_0.decompress(str_1)
            str_3 = ''
            str_4 = module_0.compress(str_3)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
