import unittest
import timeout_decorator
import ansible.plugins.connection.psrp as module_0

class Test_Psrp_7(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_3(self):
        try:
            bool_0 = True
            str_0 = '%Y'
            list_0 = [bool_0, str_0, bool_0, bool_0]
            bool_1 = False
            str_1 = 'D\\q=j\x0c/$VK2[nOzww'
            dict_0 = {str_0: str_0, str_0: bool_1, str_1: bool_0}
            connection_0 = module_0.Connection(*list_0, **dict_0)
            list_1 = None
            var_0 = connection_0.put_file(list_1, connection_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
