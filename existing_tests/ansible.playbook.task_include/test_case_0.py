import unittest
import timeout_decorator
import ansible.playbook.task_include as module_0

class Test_Task_include_1(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        try:
            bytes_0 = b'\x97`v'
            str_0 = '^GROUP=(.*)'
            str_1 = 'Rxl( 8e+ag`h(\t'
            task_include_0 = module_0.TaskInclude(str_1)
            var_0 = task_include_0.load(bytes_0, str_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
