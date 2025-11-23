import unittest
import timeout_decorator
import ansible.playbook.task as module_0
import ansible.errors as module_1

class Test_Task_26(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_8(self):
        try:
            tuple_0 = ()
            set_0 = {tuple_0, tuple_0, tuple_0, tuple_0}
            str_0 = '^ERlte|$tdCG?'
            task_0 = module_0.Task(str_0)
            var_0 = task_0.deserialize(set_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
