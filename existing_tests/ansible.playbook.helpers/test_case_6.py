import unittest
import timeout_decorator
import ansible.playbook.helpers as module_0

class Test_Helpers_7(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_6(self):
        try:
            str_0 = "=x.qUhkmBXVS8Z^'y"
            dict_0 = {str_0: str_0, str_0: str_0, str_0: str_0, str_0: str_0}
            list_0 = [dict_0]
            bool_0 = False
            bool_1 = True
            var_0 = module_0.load_list_of_roles(list_0, str_0, bool_0, bool_1)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
