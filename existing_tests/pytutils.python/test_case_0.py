import unittest
import timeout_decorator
import pytutils.python as module_0

class Test_Python_1(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        py_info_0 = module_0.PyInfo()

if __name__ == "__main__":
    unittest.main()
