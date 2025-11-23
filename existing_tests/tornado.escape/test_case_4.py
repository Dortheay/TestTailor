import unittest
import timeout_decorator
import tornado.escape as module_0

class Test_Escape_5(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_4(self):
        try:
            bytes_0 = b'\xaf\xf4\xaa\n\xba[46Gl\x1aA'
            optional_0 = module_0.utf8(bytes_0)
            any_0 = module_0.json_decode(bytes_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
