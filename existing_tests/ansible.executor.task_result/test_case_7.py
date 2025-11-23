import unittest
import timeout_decorator
import ansible.executor.task_result as module_0

class Test_Task_result_8(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        try:
            str_0 = '['
            bytes_0 = b'4pS?'
            task_result_0 = module_0.TaskResult(bytes_0, str_0, bytes_0)
            var_0 = task_result_0.needs_debugger(str_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
