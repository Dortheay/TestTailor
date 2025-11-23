import unittest
import timeout_decorator
import ansible.playbook.helpers as module_0

class Test_Helpers_4(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_3(self):
        try:
            set_0 = set()
            bool_0 = True
            tuple_0 = None
            float_0 = -1311.33653
            tuple_1 = None
            dict_0 = {tuple_0: tuple_1, bool_0: float_0}
            bool_1 = None
            str_0 = '7];L'
            list_0 = [str_0, bool_1]
            var_0 = module_0.load_list_of_blocks(bool_1, str_0, list_0)
            bool_2 = False
            str_1 = '\n        rc returns 1\n        '
            var_1 = module_0.load_list_of_blocks(float_0, dict_0, bool_2, set_0, str_1)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
