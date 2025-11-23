import unittest
import timeout_decorator
import mimesis.providers.internet as module_0
import mimesis.enums as module_1

class Test_Internet_5(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_4(self):
        try:
            port_range_0 = module_1.PortRange.EPHEMERAL
            mime_type_0 = module_1.MimeType.TEXT
            internet_0 = module_0.Internet()
            bool_0 = False
            str_0 = internet_0.ip_v4(bool_0, port_range_0)
            str_1 = internet_0.content_type(mime_type_0)
            str_2 = internet_0.ip_v4(port_range_0)
            var_0 = internet_0.stock_image()
            str_3 = 'rM09\x0c100>PyGlyR'
            int_0 = 1
            var_1 = internet_0.hashtags(int_0)
            dict_0 = {str_3: str_3, str_3: str_3}
            str_4 = internet_0.ip_v6()
            internet_1 = module_0.Internet(**dict_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
