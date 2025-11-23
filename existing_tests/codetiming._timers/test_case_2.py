import unittest
import timeout_decorator
import codetiming._timers as module_0

class Test__timers_3(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_2(self):
        timers_0 = module_0.Timers()
        str_0 = 'test_timer'
        float_0 = 2.0
        timers_0.add(str_0, float_0)
        float_1 = timers_0.mean(str_0)

if __name__ == "__main__":
    unittest.main()
