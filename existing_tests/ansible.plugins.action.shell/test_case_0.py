import unittest
import timeout_decorator
import ansible.plugins.action.shell as module_0

class Test_Shell_1(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        try:
            tuple_0 = None
            dict_0 = {}
            bool_0 = False
            bytes_0 = b'\xd6\xeb\xdc'
            bool_1 = False
            action_module_0 = module_0.ActionModule(dict_0, bool_0, dict_0, dict_0, bytes_0, bool_1)
            var_0 = action_module_0.run(tuple_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
