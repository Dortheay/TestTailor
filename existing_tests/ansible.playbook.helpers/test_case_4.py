import unittest
import timeout_decorator
import ansible.playbook.helpers as module_0

class Test_Helpers_5(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_4(self):
        try:
            int_0 = -2379
            str_0 = 'IAOofZDWd'
            list_0 = []
            var_0 = module_0.load_list_of_tasks(int_0, str_0, list_0, int_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
