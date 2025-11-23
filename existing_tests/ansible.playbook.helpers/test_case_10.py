import unittest
import timeout_decorator
import ansible.playbook.helpers as module_0

class Test_Helpers_11(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_10(self):
        try:
            str_0 = 'name'
            str_1 = 'action'
            str_2 = 'ta2k&'
            str_3 = 'debug'
            str_4 = 'tezt1'
            str_5 = {str_0: str_2, str_0: str_1, str_1: str_4, str_0: str_2, str_1: str_0}
            str_6 = ')*>[LvL<e\tRc=%E\\r@m\n'
            str_7 = 'task3'
            str_8 = '=f;zjq&v'
            str_9 = {str_0: str_7, str_1: str_3, str_3: str_8}
            str_10 = [str_5, str_6, str_9]
            str_11 = 'mocked_play'
            var_0 = None
            var_1 = None
            bool_0 = True
            var_2 = None
            var_3 = None
            var_4 = module_0.load_list_of_blocks(str_10, str_11, str_2, var_0, var_1, bool_0, var_2, var_3)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
