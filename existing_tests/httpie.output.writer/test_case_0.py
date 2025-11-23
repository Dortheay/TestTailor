import unittest
import timeout_decorator
import requests.models as module_0
import httpie.context as module_1
import argparse as module_2
import httpie.output.writer as module_3

class Test_Writer_1(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        response_0 = module_0.Response()
        str_0 = '--output'
        var_0 = response_0.__getstate__()
        environment_0 = module_1.Environment(str_0)
        namespace_0 = module_2.Namespace()
        var_1 = module_3.write_message(response_0, environment_0, namespace_0)

if __name__ == "__main__":
    unittest.main()
