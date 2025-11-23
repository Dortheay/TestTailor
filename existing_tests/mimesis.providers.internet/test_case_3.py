import unittest
import timeout_decorator
import mimesis.providers.internet as module_0
import mimesis.enums as module_1

class Test_Internet_4(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_3(self):
        try:
            internet_0 = module_0.Internet()
            str_0 = internet_0.top_level_domain()
            i_pv6_address_0 = internet_0.ip_v6_object()
            int_0 = 29
            var_0 = internet_0.hashtags(int_0)
            bool_0 = False
            var_1 = internet_0.stock_image(str_0, str_0, bool_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
