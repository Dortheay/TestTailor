import unittest
import timeout_decorator
import sty.lib as module_0

class Test_Lib_1(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        try:
            register_0 = None
            list_0 = [register_0, register_0, register_0, register_0]
            module_0.mute(*list_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
