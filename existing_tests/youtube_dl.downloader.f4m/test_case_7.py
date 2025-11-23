import unittest
import timeout_decorator
import youtube_dl.downloader.f4m as module_0

class Test_F4m_8(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_6(self):
        try:
            bytes_0 = b'\x06\x19J\xe2\xddf\xa6\xe5\x08\x1f9\xb1j\x15\xc2go'
            var_0 = module_0.read_bootstrap_info(bytes_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
