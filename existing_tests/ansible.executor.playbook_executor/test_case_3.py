import unittest
import timeout_decorator
import ansible.executor.playbook_executor as module_0
import ansible.utils.display as module_1

class Test_Playbook_executor_4(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_3(self):
        try:
            str_0 = 'listhosts'
            set_0 = set()
            int_0 = -3341
            list_0 = []
            bool_0 = False
            display_0 = module_1.Display(bool_0)
            playbook_executor_0 = module_0.PlaybookExecutor(set_0, int_0, str_0, list_0, display_0)
            var_0 = playbook_executor_0.run()
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
