import unittest
import timeout_decorator
import sanic.helpers as module_0

class Test_Helpers_7(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_6(self):
        str_0 = 'Content-Type'
        str_1 = 'Content-Length'
        str_2 = 'Content-Location'
        str_3 = 'Last-Modified'
        str_4 = 'application/json'
        str_5 = '1234'
        str_6 = 'http://example.com/resource'
        str_7 = 'Wed, 21 Oct 2015 07:28:00 GMT'
        str_8 = 'Tue, 20 Oct 2015 07:28:00 GMT'
        str_9 = {str_0: str_4, str_1: str_5, str_2: str_6, str_4: str_7, str_3: str_8}
        var_0 = module_0.remove_entity_headers(str_9)

if __name__ == "__main__":
    unittest.main()
