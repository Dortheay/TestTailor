import unittest
import timeout_decorator
import ansible.playbook.helpers as module_0

class Test_Helpers_3(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_2(self):
        try:
            bool_0 = True
            str_0 = 'Git archive command failed to create archive %s using %s directory.Error: %s'
            int_0 = -902
            var_0 = module_0.load_list_of_blocks(bool_0, str_0, int_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
