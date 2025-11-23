import unittest
import timeout_decorator
import tornado.escape as module_0

class Test_Escape_20(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_2(self):
        str_0 = 'UJ'
        str_1 = module_0.json_encode(str_0)

if __name__ == "__main__":
    unittest.main()
