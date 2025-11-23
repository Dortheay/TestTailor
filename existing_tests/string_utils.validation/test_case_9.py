import unittest
import timeout_decorator
import string_utils.validation as module_0

class Test_Validation_10(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_9(self):
        try:
            str_0 = '4111111111111111'
            str_1 = 'VISA'
            bool_0 = module_0.is_credit_card(str_0, str_1)
            str_2 = '5500000000000004'
            str_3 = 'MASTERCARD'
            bool_1 = module_0.is_credit_card(str_2, str_3)
            str_4 = '340000000000009'
            str_5 = 'AMERICAN_EXPRESS'
            bool_2 = module_0.is_credit_card(str_4, str_5)
            str_6 = '30000000000004'
            str_7 = 'DINERS_CLUB'
            bool_3 = module_0.is_credit_card(str_6, str_7)
            str_8 = '6011111111111117'
            str_9 = 'DISCOVER'
            bool_4 = module_0.is_credit_card(str_8, str_9)
            str_10 = '3530111333300000'
            str_11 = 'JCB'
            bool_5 = module_0.is_credit_card(str_10, str_11)
            bool_6 = module_0.is_credit_card(str_0)
            str_12 = '1234567812345678'
            bool_7 = module_0.is_credit_card(str_12)
            bool_8 = module_0.is_credit_card(str_0, str_3)
            str_13 = ''
            bool_9 = module_0.is_credit_card(str_13)
            int_0 = 1234567812345678
            bool_10 = module_0.is_credit_card(int_0)
            str_14 = '4111111111111111'
            str_15 = 'NON_EXISTENT_CARD'
            bool_11 = module_0.is_credit_card(str_14, str_15)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
