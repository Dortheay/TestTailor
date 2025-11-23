import unittest
import timeout_decorator
import tornado.escape as module_0

class Test_Escape_11(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_10(self):
        try:
            bytes_0 = b''
            bool_0 = False
            str_0 = '<({OL&%'
            str_1 = module_0.linkify(bytes_0)
            bool_1 = None
            dict_0 = module_0.parse_qs_bytes(bytes_0, bool_1)
            list_0 = [str_0]
            str_2 = module_0.linkify(bytes_0, bool_0, list_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
