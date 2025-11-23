import unittest
import timeout_decorator
import ansible.executor.task_result as module_0

class Test_Task_result_4(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_3(self):
        int_0 = 1335
        bool_0 = False
        str_0 = 'R~\n/}Te<NGMtS'
        float_0 = 980.95
        dict_0 = {int_0: str_0}
        task_result_0 = module_0.TaskResult(bool_0, float_0, dict_0)
        var_0 = task_result_0.is_skipped()

if __name__ == "__main__":
    unittest.main()
