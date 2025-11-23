import unittest
import timeout_decorator
import codetiming._timers as module_0

class Test__timers_12(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_5(self):
        try:
            str_0 = '2*.'
            timers_0 = module_0.Timers()
            float_0 = -221.25398127912732
            timers_0.add(str_0, float_0)
            float_1 = timers_0.stdev(str_0)
            timers_0.add(str_0, float_0)
            float_2 = timers_0.median(str_0)
            float_3 = timers_0.stdev(str_0)
            str_1 = '$+Fd%>QJxq9b'
            float_4 = -1817.2336
            timers_0.add(str_1, float_4)
            timers_0.clear()
            str_2 = 'o\nVL2!b:c P(#,J(@'
            float_5 = timers_0.total(str_2)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
