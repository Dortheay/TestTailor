import unittest
import timeout_decorator
import youtube_dl.options as module_0

class Test_Options_1(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        try:
            bytes_0 = b'\xcdz;\x7f\x18\xe3\xbd\x97\xd2u\x8e\xb2i'
            var_0 = module_0.parseOpts(bytes_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
