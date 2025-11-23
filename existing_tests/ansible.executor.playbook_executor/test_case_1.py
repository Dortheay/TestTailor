import unittest
import timeout_decorator
import ansible.executor.playbook_executor as module_0
import ansible.utils.display as module_1

class Test_Playbook_executor_2(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        try:
            float_0 = -759.869
            tuple_0 = (float_0,)
            list_0 = []
            str_0 = None
            display_0 = module_1.Display()
            str_1 = '?Qf'
            playbook_executor_0 = module_0.PlaybookExecutor(list_0, str_0, display_0, str_1, tuple_0)
            var_0 = playbook_executor_0.run()
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
