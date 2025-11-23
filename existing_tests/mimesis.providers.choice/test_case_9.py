import unittest
import timeout_decorator
import mimesis.providers.choice as module_0

class Test_Choice_10(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_7(self):
        try:
            optional_0 = None
            choice_0 = module_0.Choice()
            list_0 = [optional_0]
            int_0 = -1325
            bool_0 = True
            list_1 = [optional_0]
            bytes_0 = b''
            choice_1 = module_0.Choice(*list_1)
            dict_0 = None
            str_0 = ')r3*q,'
            tuple_0 = (str_0,)
            int_1 = 676
            str_1 = '?I/@t&}lAtE~\\_L+'
            choice_2 = module_0.Choice()
            dict_1 = {int_1: dict_0, str_1: choice_2, int_1: bool_0, dict_0: tuple_0}
            tuple_1 = (dict_0, tuple_0, str_0, dict_1)
            str_2 = 'RP'
            float_0 = 2808.334292
            tuple_2 = (tuple_1, str_2, float_0, bytes_0)
            var_0 = choice_0.__call__(tuple_2, bool_0)
            var_1 = choice_1.__call__(list_0, int_0, bool_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
