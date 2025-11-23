import unittest
import timeout_decorator
import httpie.context as module_0
import argparse as module_1
import httpie.output.writer as module_2
import typing as module_3
import httpie.models as module_4
import httpie.output.streams as module_5
import requests.models as module_6

class Test_Writer_7(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_5(self):
        try:
            prepared_request_0 = module_6.PreparedRequest()
            environment_0 = module_0.Environment()
            str_0 = 'XT"9%F#:'
            str_1 = '#0087ff'
            str_2 = 'uL'
            dict_0 = {str_0: prepared_request_0, str_1: str_0, str_2: environment_0, str_0: str_1}
            namespace_0 = module_1.Namespace(**dict_0)
            var_0 = module_2.write_message(prepared_request_0, environment_0, namespace_0, namespace_0, dict_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
