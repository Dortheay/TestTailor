import unittest
import timeout_decorator
import ansible.plugins.callback.tree as module_0

class Test_Tree_5(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_3(self):
        try:
            str_0 = 'KH.4\x0bX{\x0c;I\x0c]P9'
            callback_module_0 = module_0.CallbackModule()
            var_0 = callback_module_0.v2_runner_on_failed(str_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
