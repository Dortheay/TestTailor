import unittest
import timeout_decorator
import ansible.plugins.callback.tree as module_0

class Test_Tree_6(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_4(self):
        try:
            str_0 = 'OsG#j</+3HW'
            callback_module_0 = module_0.CallbackModule()
            var_0 = callback_module_0.v2_runner_on_unreachable(str_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
