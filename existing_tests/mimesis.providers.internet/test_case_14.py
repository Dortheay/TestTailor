import unittest
import timeout_decorator
import mimesis.providers.internet as module_0
import mimesis.enums as module_1

class Test_Internet_15(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_8(self):
        internet_0 = module_0.Internet()
        optional_0 = None
        str_0 = internet_0.content_type(optional_0)
        str_1 = internet_0.top_level_domain()
        str_2 = internet_0.home_page()
        str_3 = internet_0.user_agent()
        str_4 = internet_0.user_agent()
        str_5 = internet_0.ip_v6()

if __name__ == "__main__":
    unittest.main()
