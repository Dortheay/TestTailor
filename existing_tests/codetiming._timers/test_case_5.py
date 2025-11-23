import unittest
import timeout_decorator
import codetiming._timers as module_0

class Test__timers_6(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_5(self):
        timers_0 = module_0.Timers()
        str_0 = 'test_timer'
        float_0 = 1.0
        timers_0.add(str_0, float_0)
        float_1 = timers_0.min(str_0)
        float_2 = 3.0
        timers_0.add(str_0, float_2)

if __name__ == "__main__":
    unittest.main()
