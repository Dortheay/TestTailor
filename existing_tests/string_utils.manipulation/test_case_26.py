import unittest
import timeout_decorator
import string_utils.manipulation as module_0

class Test_Manipulation_27(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_15(self):
        try:
            str_0 = '%<:\r gtW>^i6Dpah'
            str_1 = module_0.asciify(str_0)
            str_2 = None
            str_3 = '\n    Checks if a string is a valid credit card number.\n    If card type is provided then it checks against that specific type only,\n    otherwise any known credit card number will be accepted.\n\n    Supported card types are the following:\n\n    - VISA\n    - MASTERCARD\n    - AMERICAN_EXPRESS\n    - DINERS_CLUB\n    - DISCOVER\n    - JCB\n\n    :param input_string: String to check.\n    :type input_string: str\n    :param card_type: Card type. Default to None (any card).\n    :type card_type: str\n\n    :return: True if credit card, false otherwise.\n    '
            str_4 = module_0.reverse(str_3)
            str_5 = module_0.strip_margin(str_2)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
