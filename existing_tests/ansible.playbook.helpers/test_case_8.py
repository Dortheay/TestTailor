import unittest
import timeout_decorator
import ansible.playbook.helpers as module_0

class Test_Helpers_9(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_8(self):
        try:
            str_0 = 'name'
            str_1 = 'action'
            str_2 = 'msg'
            str_3 = 'task1'
            str_4 = 'debug'
            str_5 = 'test1'
            str_6 = {str_0: str_3, str_1: str_4, str_2: str_5}
            str_7 = 'KlocX'
            str_8 = [str_2]
            str_9 = {str_7: str_8}
            str_10 = 'task3'
            str_11 = 'test3'
            str_12 = {str_0: str_10, str_1: str_4, str_2: str_11}
            str_13 = [str_6, str_9, str_12]
            str_14 = 'mocked_play'
            var_0 = None
            var_1 = None
            var_2 = None
            bool_0 = False
            var_3 = None
            var_4 = module_0.load_list_of_blocks(str_13, str_14, var_0, var_1, var_2, bool_0, str_0, var_3)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
