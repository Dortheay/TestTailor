import unittest
import timeout_decorator
import ansible.plugins.callback.tree as module_0

class Test_Tree_2(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        try:
            set_0 = set()
            callback_module_0 = module_0.CallbackModule(set_0, set_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
