import unittest
import timeout_decorator
import ansible.playbook.handler_task_include as module_0

class Test_Handler_task_include_1(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        try:
            str_0 = 'JiUcu4S\\A+aB'
            set_0 = None
            handler_task_include_0 = module_0.HandlerTaskInclude()
            var_0 = handler_task_include_0.load(str_0, set_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
