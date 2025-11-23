import unittest
import timeout_decorator
import mimesis.providers.payment as module_0
import mimesis.enums as module_1

class Test_Payment_2(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        payment_0 = module_0.Payment()
        str_0 = payment_0.credit_card_number()
        int_0 = payment_0.cid()
        str_1 = payment_0.paypal()

if __name__ == "__main__":
    unittest.main()
