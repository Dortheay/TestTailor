import unittest
import timeout_decorator
import ansible.plugins.filter.core as module_0

class Test_Core_76(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_26(self):
        str_0 = 'name'
        str_1 = 'groups'
        str_2 = 'authorized'
        str_3 = 'alice'
        str_4 = 'wheel'
        str_5 = [str_4, str_4]
        str_6 = [str_2]
        str_7 = {str_0: str_3, str_1: str_5, str_2: str_6}
        str_8 = [str_6, str_3]
        str_9 = 'Tf{FB@i1UKcU-_y8r/L'
        str_10 = [str_9]
        str_11 = {str_0: str_6, str_1: str_8, str_2: str_10}
        str_12 = [str_7, str_11]
        var_0 = module_0.subelements(str_12, str_1)
        str_13 = [str_4]
        str_14 = [str_6]
        str_15 = {str_0: str_3, str_1: str_13, str_2: str_14}
        str_16 = [str_9]
        str_17 = {str_0: str_2, str_2: str_16}
        str_18 = [str_15, str_17]
        bool_0 = True
        var_1 = module_0.subelements(str_18, str_1, bool_0)

if __name__ == "__main__":
    unittest.main()
