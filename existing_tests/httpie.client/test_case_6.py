import unittest
import timeout_decorator
import httpie.cli.dicts as module_0
import httpie.client as module_1
import argparse as module_2

class Test_Client_7(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        pass

if __name__ == "__main__":
    unittest.main()
