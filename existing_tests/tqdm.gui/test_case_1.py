import unittest
import timeout_decorator
import tqdm.gui as module_0

class Test_Gui_2(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        try:
            var_0 = module_0.tgrange()
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
