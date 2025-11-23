import unittest
import timeout_decorator
import httpie.context as module_0
import argparse as module_1
import httpie.output.writer as module_2
import typing as module_3
import httpie.models as module_4
import httpie.output.streams as module_5
import requests.models as module_6

class Test_Writer_3(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        try:
            str_0 = '--output'
            environment_0 = module_0.Environment(str_0)
            namespace_0 = module_1.Namespace()
            response_0 = None
            var_0 = environment_0.__repr__()
            var_1 = module_2.write_message(response_0, environment_0, namespace_0, namespace_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
