import unittest
import timeout_decorator
import youtube_dl.downloader.fragment as module_0

class Test_Fragment_1(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        try:
            bytes_0 = b'\x04\xd3\xf1*k\x95\xe2\x08n\xb2\xd0p1'
            list_0 = [bytes_0, bytes_0, bytes_0]
            str_0 = 'w!=ddBkt'
            bool_0 = False
            bytes_1 = b'5\xc8\xf7[_\xf8\x8bn\x14\xb9Dw\xe3\xe8\xd7Zh\x87\xe0'
            str_1 = '\n8GYX|r;uU/7'
            fragment_f_d_0 = module_0.FragmentFD(bytes_1, str_1)
            var_0 = fragment_f_d_0.report_retry_fragment(bytes_0, list_0, str_0, bool_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
