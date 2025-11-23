import unittest
import timeout_decorator
import ansible.plugins.lookup.vars as module_0

class Test_Vars_3(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        try:
            str_0 = 'WARNWEEKS'
            str_1 = '.~">*xUKNY\x0ctKqCH\\0)'
            list_0 = [str_1]
            int_0 = 2225
            tuple_0 = (str_0, str_1, list_0, int_0)
            int_1 = -2140
            str_2 = 'UaM\tD?=$'
            str_3 = 'OHh+~26.aVcfWVT&8C@~'
            tuple_1 = (list_0, str_2, int_1, str_3)
            dict_0 = {str_0: str_0, str_1: tuple_1, str_3: str_2, str_1: int_0}
            lookup_module_0 = module_0.LookupModule()
            var_0 = lookup_module_0.run(tuple_0, int_1, **dict_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
