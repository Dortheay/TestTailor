import unittest
import timeout_decorator
import tornado.escape as module_0

class Test_Escape_2(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        try:
            bytes_0 = b'\xc7'
            any_0 = module_0.json_decode(bytes_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
