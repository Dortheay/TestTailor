import unittest
import timeout_decorator
import ansible.plugins.callback.tree as module_0

class Test_Tree_4(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_2(self):
        try:
            float_0 = 4425.6
            callback_module_0 = module_0.CallbackModule()
            var_0 = callback_module_0.v2_runner_on_ok(float_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
