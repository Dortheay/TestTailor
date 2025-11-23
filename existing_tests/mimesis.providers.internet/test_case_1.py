import unittest
import timeout_decorator
import mimesis.providers.internet as module_0
import mimesis.enums as module_1

class Test_Internet_2(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        try:
            internet_0 = module_0.Internet()
            str_0 = internet_0.ip_v4()
            internet_1 = module_0.Internet()
            str_1 = '100 Continue'
            str_2 = internet_0.http_status_message()
            str_3 = internet_1.content_type(str_1)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
