import unittest
import timeout_decorator
import mimesis.providers.payment as module_0

class Test_Payment_8(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        try:
            payment_0 = module_0.Payment()
            str_0 = 'kD+a'
            str_1 = payment_0.credit_card_number(str_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
