import unittest
import timeout_decorator
import thonny.roughparse as module_0

class Test_Roughparse_13(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_6(self):
        try:
            str_0 = 'Used when an ancestor class method has an __init__ method which is not called by a derived class.'
            str_1 = ';|'
            list_0 = [str_0]
            hyper_parser_0 = module_0.HyperParser(str_1, list_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
