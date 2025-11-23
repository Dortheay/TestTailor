import unittest
import timeout_decorator
import ansible.playbook.handler_task_include as module_0

class Test_Handler_task_include_2(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        handler_task_include_0 = module_0.HandlerTaskInclude()

if __name__ == "__main__":
    unittest.main()
