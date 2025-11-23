import unittest
import timeout_decorator
import apimd.loader as module_0

class Test_Loader_8(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_4(self):
        str_0 = 'n'
        bool_0 = False
        int_0 = None
        str_1 = module_0.loader(str_0, str_0, bool_0, int_0, bool_0)

if __name__ == "__main__":
    unittest.main()
