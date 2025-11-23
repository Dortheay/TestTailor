import unittest
import timeout_decorator
import sanic.headers as module_0

class Test_Headers_3(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_2(self):
        try:
            iterable_0 = None
            dict_0 = module_0.fwd_normalize(iterable_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
