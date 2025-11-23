import unittest
import timeout_decorator
import codetiming._timers as module_0

class Test__timers_8(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        try:
            str_0 = 'OTYk$5m=!'
            float_0 = -3155.89
            timers_0 = module_0.Timers()
            timers_0.__setitem__(str_0, float_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
