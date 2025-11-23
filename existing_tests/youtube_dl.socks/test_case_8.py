import unittest
import timeout_decorator
import youtube_dl.socks as module_0

class Test_Socks_9(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_2(self):
        int_0 = 5
        int_1 = 4
        invalid_version_error_0 = module_0.InvalidVersionError(int_0, int_1)
        var_0 = str(invalid_version_error_0)

if __name__ == "__main__":
    unittest.main()
