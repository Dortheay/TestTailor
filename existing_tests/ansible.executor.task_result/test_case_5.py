import unittest
import timeout_decorator
import ansible.executor.task_result as module_0

class Test_Task_result_6(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_5(self):
        str_0 = ''
        dict_0 = {str_0: str_0}
        float_0 = -377.6814
        tuple_0 = (float_0,)
        bytes_0 = None
        task_result_0 = module_0.TaskResult(tuple_0, bytes_0, dict_0)
        bool_0 = True
        var_0 = task_result_0.needs_debugger(bool_0)

if __name__ == "__main__":
    unittest.main()
