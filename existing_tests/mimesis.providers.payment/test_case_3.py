import unittest
import timeout_decorator
import mimesis.providers.payment as module_0
import mimesis.enums as module_1

class Test_Payment_4(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_3(self):
        payment_0 = module_0.Payment()
        int_0 = payment_0.cvv()
        payment_1 = module_0.Payment()
        str_0 = payment_0.ethereum_address()
        str_1 = payment_1.bitcoin_address()
        payment_2 = module_0.Payment()
        str_2 = payment_1.ethereum_address()
        str_3 = payment_1.credit_card_number()

if __name__ == "__main__":
    unittest.main()
