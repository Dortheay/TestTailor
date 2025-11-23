import unittest
import timeout_decorator
import codetiming._timers as module_0

class Test__timers_11(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_4(self):
        try:
            str_0 = "S_&'g>TeH"
            timers_0 = module_0.Timers()
            float_0 = timers_0.stdev(str_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
