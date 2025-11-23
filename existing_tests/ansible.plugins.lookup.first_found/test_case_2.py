import unittest
import timeout_decorator
import ansible.plugins.lookup.first_found as module_0

class Test_First_found_3(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_2(self):
        try:
            str_0 = '\tmJWe '
            str_1 = "'F7LtWXsX@G\ro[*#:m"
            str_2 = 'I<-7'
            dict_0 = {str_0: str_0, str_1: str_1, str_2: str_1}
            list_0 = [dict_0, str_0, str_1]
            str_3 = ',\x0c18.d}bg50S[#ewYx'
            int_0 = 1940
            str_4 = '6"iUjAD}/?K'
            str_5 = "'*sjU&extsq'RUJ\x0c\n"
            dict_1 = {str_4: int_0, str_5: str_5, str_5: str_5}
            lookup_module_0 = module_0.LookupModule(list_0, **dict_1)
            var_0 = lookup_module_0.run(list_0, str_3)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
