import unittest
import timeout_decorator
import sanic.helpers as module_0

class Test_Helpers_6(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_5(self):
        str_0 = 'Content-Type'
        str_1 = 'Content-Location'
        str_2 = 'Expires'
        str_3 = 'Content-Length'
        str_4 = 'Last-Modified'
        str_5 = 'Wed, 21 Oct 2025 07:28:00 GMT'
        str_6 = '1234'
        str_7 = {str_0: str_2, str_1: str_4, str_2: str_5, str_3: str_6, str_4: str_0}
        str_8 = (str_1, str_2)
        var_0 = module_0.remove_entity_headers(str_7, str_8)

if __name__ == "__main__":
    unittest.main()
