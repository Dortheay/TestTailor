import unittest
import timeout_decorator
import tornado.concurrent as module_0
import concurrent.futures._base as module_1

class Test_Concurrent_2(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        str_0 = '9h.B\rNT3MVGp~K"7iF'
        bool_0 = module_0.is_future(str_0)

if __name__ == "__main__":
    unittest.main()
