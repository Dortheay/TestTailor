import unittest
import timeout_decorator
import ansible.executor.task_result as module_0

class Test_Task_result_1(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        str_0 = '/0^n'
        bytes_0 = b'4pS?'
        task_result_0 = module_0.TaskResult(bytes_0, str_0, bytes_0)

if __name__ == "__main__":
    unittest.main()
