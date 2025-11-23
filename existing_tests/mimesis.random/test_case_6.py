import unittest
import timeout_decorator
import mimesis.random as module_0

class Test_Random_7(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_6(self):
        str_0 = 'pGIxB!MGO1dj@N#'
        float_0 = 1.5
        set_0 = {float_0, str_0, float_0}
        str_1 = '4'
        tuple_0 = (str_0, float_0, set_0, str_1)
        any_0 = module_0.get_random_item(tuple_0)

if __name__ == "__main__":
    unittest.main()
