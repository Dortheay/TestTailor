import unittest
import timeout_decorator
import typesystem.fields as module_0
import decimal as module_1

class Test_Fields_108(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_22(self):
        str_0 = 'm8dgt'
        str_1 = None
        dict_0 = {str_0: str_0, str_1: str_0}
        choice_0 = module_0.Choice(choices=dict_0)

if __name__ == "__main__":
    unittest.main()
