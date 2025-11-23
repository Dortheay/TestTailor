import unittest
import timeout_decorator
import pytutils.files as module_0

class Test_Files_1(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        try:
            list_0 = None
            set_0 = {list_0, list_0, list_0}
            var_0 = module_0.burp(list_0, list_0, set_0, set_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
