import unittest
import timeout_decorator
import codetiming._timers as module_0

class Test__timers_9(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_2(self):
        try:
            str_0 = ':/L6@'
            timers_0 = module_0.Timers()
            float_0 = timers_0.total(str_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
