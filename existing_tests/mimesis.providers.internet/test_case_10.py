import unittest
import timeout_decorator
import mimesis.providers.internet as module_0
import mimesis.enums as module_1

class Test_Internet_11(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_4(self):
        t_l_d_type_0 = module_1.TLDType.GEOTLD
        internet_0 = module_0.Internet()
        i_pv4_address_0 = internet_0.ip_v4_object()
        str_0 = internet_0.ip_v6()
        list_0 = [t_l_d_type_0]
        internet_1 = module_0.Internet(*list_0)
        var_0 = internet_0.stock_image()

if __name__ == "__main__":
    unittest.main()
