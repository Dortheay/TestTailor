import unittest
import timeout_decorator
import ansible.playbook.helpers as module_0

class Test_Helpers_1(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        try:
            int_0 = 2093
            bool_0 = True
            str_0 = '3sqWRgN47EaO1x'
            var_0 = module_0.load_list_of_roles(int_0, bool_0, str_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
