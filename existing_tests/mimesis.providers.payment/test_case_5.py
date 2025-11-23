import unittest
import timeout_decorator
import mimesis.providers.payment as module_0
import mimesis.enums as module_1

class Test_Payment_6(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_5(self):
        payment_0 = module_0.Payment()
        dict_0 = payment_0.credit_card_owner()

if __name__ == "__main__":
    unittest.main()
