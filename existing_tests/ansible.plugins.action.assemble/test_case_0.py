import unittest
import timeout_decorator
import ansible.plugins.action.assemble as module_0

class Test_Assemble_1(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        try:
            action_module_0 = module_0.ActionModule()
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
