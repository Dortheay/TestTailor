import unittest
import timeout_decorator
import pypara.monetary as module_0
import decimal as module_1
import pypara.currencies as module_2

class Test_Monetary_18(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_17(self):
        try:
            int_0 = 3242
            str_0 = ''
            bytes_0 = b'\xe787#\xb3\x0e\xc0\x06\x8e\xe2\xbb\xb9'
            list_0 = [str_0, int_0, str_0]
            some_price_0 = module_0.SomePrice(*list_0)
            price_0 = some_price_0.scalar_add(bytes_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
