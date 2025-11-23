import unittest
import timeout_decorator
import argparse as module_0
import requests.models as module_1
import httpie.core as module_2
import httpie.context as module_3

class Test_Core_6(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        try:
            namespace_0 = module_0.Namespace()
            environment_0 = module_3.Environment()
            exit_status_0 = module_2.program(namespace_0, environment_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
