import unittest
import timeout_decorator
import mimesis.providers.payment as module_0
import mimesis.enums as module_1

class Test_Payment_3(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_2(self):
        payment_0 = module_0.Payment()
        dict_0 = payment_0.credit_card_owner()
        payment_1 = module_0.Payment()
        int_0 = payment_1.cvv()
        str_0 = payment_1.bitcoin_address()
        int_1 = payment_1.cvv()

if __name__ == "__main__":
    unittest.main()
