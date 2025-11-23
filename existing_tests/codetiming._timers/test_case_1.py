import unittest
import timeout_decorator
import codetiming._timers as module_0

class Test__timers_2(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        str_0 = "`f')^FQv"
        float_0 = 523.5474
        timers_0 = module_0.Timers()
        timers_0.add(str_0, float_0)

if __name__ == "__main__":
    unittest.main()
