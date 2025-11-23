import unittest
import timeout_decorator
import ansible.executor.task_result as module_0

class Test_Task_result_5(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_4(self):
        bytes_0 = b'\xed\x91sNt\x02l\x1b\x914\xb5(QY\x07:'
        str_0 = ''
        bytes_1 = b'4pS?'
        task_result_0 = module_0.TaskResult(bytes_0, str_0, bytes_1)
        var_0 = task_result_0.needs_debugger()

if __name__ == "__main__":
    unittest.main()
