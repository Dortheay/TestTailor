import unittest
import timeout_decorator
import ansible.playbook.task as module_0
import ansible.errors as module_1

class Test_Task_41(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_23(self):
        try:
            str_0 = 'become_flags'
            list_0 = None
            task_0 = module_0.Task()
            var_0 = task_0.get_first_parent_include()
            bool_0 = False
            dict_0 = {bool_0: list_0, str_0: str_0, bool_0: str_0}
            str_1 = 'z=2"o1\r@.h\ru=T8)c*'
            set_0 = set()
            var_1 = task_0.get_include_params()
            int_0 = 513
            var_2 = task_0.copy()
            task_1 = module_0.Task(str_1, set_0, int_0)
            var_3 = task_1.__repr__()
            task_2 = module_0.Task(bool_0, dict_0)
            var_4 = task_2.serialize()
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
