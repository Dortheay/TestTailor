import unittest
import timeout_decorator
import tqdm.gui as module_0

class Test_Gui_1(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        try:
            tqdm_gui_0 = module_0.tqdm_gui()
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
