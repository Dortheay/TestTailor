import unittest
import timeout_decorator
import sty.lib as module_0

class Test_Lib_4(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        module_0.mute()

if __name__ == "__main__":
    unittest.main()
