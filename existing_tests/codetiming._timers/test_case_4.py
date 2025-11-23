import unittest
import timeout_decorator
import codetiming._timers as module_0

class Test__timers_5(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_4(self):
        timers_0 = module_0.Timers()
        str_0 = 'example_timer'
        float_0 = 5.0
        timers_0.add(str_0, float_0)
        float_1 = 3.0
        timers_0.add(str_0, float_1)
        float_2 = 7.0
        timers_0.add(str_0, float_2)
        float_3 = timers_0.median(str_0)

if __name__ == "__main__":
    unittest.main()
