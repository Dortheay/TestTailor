import unittest
import timeout_decorator
import codetiming._timers as module_0

class Test__timers_10(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_3(self):
        try:
            timers_0 = module_0.Timers()
            timers_0.clear()
            str_0 = '\nB\rmYq8q\r'
            float_0 = timers_0.count(str_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
