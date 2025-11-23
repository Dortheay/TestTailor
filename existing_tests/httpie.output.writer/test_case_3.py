import unittest
import timeout_decorator
import httpie.context as module_0
import argparse as module_1
import httpie.output.writer as module_2
import typing as module_3
import httpie.models as module_4
import httpie.output.streams as module_5
import requests.models as module_6

class Test_Writer_4(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_2(self):
        try:
            environment_0 = module_0.Environment()
            namespace_0 = module_1.Namespace()
            base_stream_0 = None
            i_o_0 = module_3.IO()
            bool_0 = True
            var_0 = module_2.write_stream(base_stream_0, i_o_0, bool_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
