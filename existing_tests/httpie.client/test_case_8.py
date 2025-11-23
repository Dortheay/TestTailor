import unittest
import timeout_decorator
import httpie.cli.dicts as module_0
import httpie.client as module_1
import argparse as module_2

class Test_Client_9(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_2(self):
        str_0 = '$\t72UD8&*}MUbL'
        str_1 = ''
        str_2 = module_1.ensure_path_as_is(str_0, str_1)

if __name__ == "__main__":
    unittest.main()
