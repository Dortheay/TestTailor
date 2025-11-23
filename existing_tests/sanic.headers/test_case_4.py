import unittest
import timeout_decorator
import sanic.headers as module_0

class Test_Headers_5(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_4(self):
        try:
            int_0 = 618
            iterable_0 = None
            bytes_0 = module_0.format_http1_response(int_0, iterable_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
