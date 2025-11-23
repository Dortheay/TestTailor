import unittest
import timeout_decorator
import ansible.plugins.callback.default as module_0

class Test_Default_1(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        callback_module_0 = module_0.CallbackModule()

if __name__ == "__main__":
    unittest.main()
