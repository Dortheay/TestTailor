import unittest
import timeout_decorator
import argparse as module_0
import py_backwards.conf as module_1

class Test_Conf_2(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        try:
            namespace_0 = module_0.Namespace()
            module_1.init_settings(namespace_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
