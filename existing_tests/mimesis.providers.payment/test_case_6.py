import unittest
import timeout_decorator
import mimesis.providers.payment as module_0
import mimesis.enums as module_1

class Test_Payment_7(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_6(self):
        payment_0 = module_0.Payment()
        int_0 = payment_0.cid()
        str_0 = payment_0.bitcoin_address()
        card_type_0 = module_1.CardType.VISA
        str_1 = payment_0.credit_card_number(card_type_0)
        payment_1 = module_0.Payment()
        str_2 = payment_1.paypal()
        str_3 = payment_1.credit_card_number()

if __name__ == "__main__":
    unittest.main()
