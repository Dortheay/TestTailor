import unittest
import timeout_decorator
import youtube_dl.socks as module_0

class Test_Socks_6(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_5(self):
        try:
            sockssocket_0 = module_0.sockssocket()
            int_0 = 10
            var_0 = sockssocket_0.recvall(int_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
