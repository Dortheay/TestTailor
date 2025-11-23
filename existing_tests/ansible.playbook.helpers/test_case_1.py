import unittest
import timeout_decorator
import ansible.playbook.helpers as module_0

class Test_Helpers_2(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        try:
            bool_0 = False
            list_0 = [bool_0, bool_0, bool_0]
            float_0 = 581.8
            str_0 = '*.l'
            var_0 = module_0.load_list_of_blocks(list_0, float_0, str_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
