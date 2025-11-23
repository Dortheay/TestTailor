import unittest
import timeout_decorator
import sty.lib as module_0

class Test_Lib_2(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        try:
            var_0 = object()
            str_0 = '"W\t\tsa'
            list_0 = [str_0]
            module_0.unmute(*list_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
