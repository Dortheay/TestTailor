import unittest
import timeout_decorator
import codetiming._timers as module_0

class Test__timers_1(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        timers_0 = module_0.Timers()

if __name__ == "__main__":
    unittest.main()
