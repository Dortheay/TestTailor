import unittest
import timeout_decorator
import argparse as module_0
import requests.models as module_1
import httpie.core as module_2
import httpie.context as module_3

class Test_Core_5(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        try:
            namespace_0 = module_0.Namespace()
            response_0 = module_1.Response()
            tuple_0 = module_2.get_output_options(namespace_0, response_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
