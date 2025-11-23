import unittest
import timeout_decorator
import ansible.plugins.action.shell as module_0

class Test_Shell_2(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        bool_0 = None
        dict_0 = {bool_0: bool_0, bool_0: bool_0, bool_0: bool_0, bool_0: bool_0}
        bytes_0 = b'\xd6\x12\x82q\xaeBx3\x9fJ\x1e\xfc&\x0f'
        set_0 = set()
        action_module_0 = module_0.ActionModule(bool_0, bool_0, dict_0, bytes_0, dict_0, set_0)

if __name__ == "__main__":
    unittest.main()
