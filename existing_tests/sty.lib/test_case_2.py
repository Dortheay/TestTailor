import unittest
import timeout_decorator
import sty.lib as module_0

class Test_Lib_3(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        module_0.unmute()

if __name__ == "__main__":
    unittest.main()
