import unittest
import timeout_decorator
import mimesis.providers.internet as module_0
import mimesis.enums as module_1

class Test_Internet_1(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        try:
            str_0 = 'zWNJH>zbP'
            float_0 = None
            list_0 = []
            internet_0 = module_0.Internet(*list_0)
            var_0 = internet_0.stock_image(str_0, float_0)
            str_1 = internet_0.image_placeholder()
            internet_1 = module_0.Internet()
            str_2 = internet_1.http_method()
            i_pv6_address_0 = internet_1.ip_v6_object()
            str_3 = internet_1.top_level_domain()
            dict_0 = None
            str_4 = internet_1.ip_v6()
            i_pv6_address_1 = internet_1.ip_v6_object()
            str_5 = internet_1.emoji()
            int_0 = internet_1.port()
            str_6 = internet_0.ip_v6()
            internet_2 = module_0.Internet(*list_0, **dict_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
