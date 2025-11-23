import unittest
import timeout_decorator
import thefuck.rules.lein_not_task as module_0

class Test_Lein_not_task_1(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        try:
            list_0 = None
            var_0 = module_0.get_new_command(list_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
