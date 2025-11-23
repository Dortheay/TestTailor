import unittest
import timeout_decorator
import argparse as module_0
import requests.models as module_1
import httpie.core as module_2
import httpie.context as module_3

class Test_Core_7(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_2(self):
        try:
            bytes_0 = b'Z\xf9\xc4\x99\xf7}\x11\xc3\xcc\x11p8\xbc'
            list_0 = [bytes_0, bytes_0]
            str_0 = 'SSL'
            list_1 = module_2.decode_raw_args(list_0, str_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
