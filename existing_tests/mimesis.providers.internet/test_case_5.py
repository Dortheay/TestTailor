import unittest
import timeout_decorator
import mimesis.providers.internet as module_0
import mimesis.enums as module_1

class Test_Internet_6(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_5(self):
        try:
            var_0 = None
            list_0 = [var_0]
            internet_0 = module_0.Internet(*list_0)
            int_0 = internet_0.port()
            i_pv6_address_0 = internet_0.ip_v6_object()
            str_0 = internet_0.ip_v4()
            list_1 = []
            internet_1 = module_0.Internet(*list_1)
            str_1 = internet_1.ip_v4()
            str_2 = internet_1.home_page()
            str_3 = internet_1.emoji()
            internet_2 = module_0.Internet()
            internet_3 = module_0.Internet(*list_0)
            var_1 = internet_1.stock_image()
            var_2 = internet_3.hashtags()
            str_4 = internet_2.emoji()
            port_range_0 = None
            internet_4 = module_0.Internet(*list_1)
            int_1 = internet_4.port(port_range_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
