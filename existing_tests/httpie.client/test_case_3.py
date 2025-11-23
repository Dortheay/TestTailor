import unittest
import timeout_decorator
import httpie.client as module_0
import argparse as module_1
import pathlib as module_2
import httpie.cli.dicts as module_3

class Test_Client_4(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_3(self):
        try:
            namespace_0 = None
            dict_0 = module_0.make_send_kwargs(namespace_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
