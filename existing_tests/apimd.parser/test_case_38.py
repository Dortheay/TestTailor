import unittest
import timeout_decorator
import ast as module_0
import apimd.parser as module_1
import collections.abc as module_2

class Test_Parser_39(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_22(self):
        try:
            str_0 = 'R{j_6O6iu!j_'
            str_1 = module_1.doctest(str_0)
            list_0 = []
            iterable_0 = None
            str_2 = module_1.table(*list_0, items=iterable_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
