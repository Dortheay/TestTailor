import unittest
import timeout_decorator
import ansible.playbook.task_include as module_0

class Test_Task_include_6(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_2(self):
        int_0 = -2646
        task_include_0 = module_0.TaskInclude(int_0)
        var_0 = task_include_0.build_parent_block()

if __name__ == "__main__":
    unittest.main()
