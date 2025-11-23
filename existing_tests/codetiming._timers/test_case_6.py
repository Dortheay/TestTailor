import unittest
import timeout_decorator
import codetiming._timers as module_0

class Test__timers_7(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        try:
            timers_0 = module_0.Timers()
            timers_0.clear()
            str_0 = 'Timer is running. Use .stop() to stop it'
            float_0 = -3741.7216
            float_1 = timers_0.apply(float_0, str_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
