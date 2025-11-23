import unittest
import timeout_decorator
import youtube_dl.socks as module_0

class Test_Socks_10(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_3(self):
        sockssocket_0 = module_0.sockssocket()

if __name__ == "__main__":
    unittest.main()
