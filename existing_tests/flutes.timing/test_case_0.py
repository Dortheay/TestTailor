import unittest
import timeout_decorator
import flutes.timing as module_0

class Test_Timing_1(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        var_0 = module_0.work_in_progress()

if __name__ == "__main__":
    unittest.main()
