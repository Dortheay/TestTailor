import unittest
import timeout_decorator
import ansible.plugins.filter.core as module_0

class Test_Core_5(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_4(self):
        try:
            str_0 = ',{BBv!l4g>ibr*@eLf87'
            str_1 = None
            str_2 = 'R'
            dict_0 = {str_0: str_0, str_1: str_1, str_1: str_1, str_2: str_2}
            tuple_0 = (dict_0,)
            str_3 = 'Z-ntGG}?\r]:\nnR'
            var_0 = module_0.regex_findall(tuple_0, tuple_0, str_3)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
