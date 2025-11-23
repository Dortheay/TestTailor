import unittest
import timeout_decorator
import codetiming._timers as module_0

class Test__timers_4(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_3(self):
        str_0 = '2*.'
        timers_0 = module_0.Timers()
        float_0 = -221.25398127912732
        timers_0.add(str_0, float_0)
        float_1 = timers_0.stdev(str_0)
        float_2 = timers_0.max(str_0)

if __name__ == "__main__":
    unittest.main()
