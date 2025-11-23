import unittest
import timeout_decorator
import ansible.plugins.connection.psrp as module_0

class Test_Psrp_6(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_2(self):
        try:
            list_0 = None
            dict_0 = {list_0: list_0}
            list_1 = [dict_0, list_0, dict_0]
            connection_0 = module_0.Connection(*list_1)
            var_0 = connection_0.close()
            bool_0 = True
            str_0 = '%Y'
            list_2 = [bool_0, str_0, bool_0, bool_0]
            bool_1 = False
            str_1 = 'D\\q=j\x0c/$VK2[nOzww'
            dict_1 = {str_0: str_0, str_0: bool_1, str_1: bool_0}
            connection_1 = module_0.Connection(*list_2, **dict_1)
            float_0 = 467.5382
            tuple_0 = ()
            tuple_1 = (float_0, tuple_0)
            str_2 = '%W'
            var_1 = connection_1.fetch_file(tuple_1, str_2)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
