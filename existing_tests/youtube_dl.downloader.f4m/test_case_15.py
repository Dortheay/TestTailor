import unittest
import timeout_decorator
import youtube_dl.downloader.f4m as module_0

class Test_F4m_16(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_14(self):
        try:
            bytes_0 = b'\x06\x19\xafJ\xe2\xdd\xa6\xe5\x08\x1f9\xb1j\x15\xc2go'
            dict_0 = {bytes_0: bytes_0}
            str_0 = 'H'
            var_0 = module_0.write_unsigned_int(dict_0, str_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
