import unittest
import timeout_decorator
import ansible.plugins.action.copy as module_0

class Test_Copy_3(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        str_0 = '}s@5EJ.*xQn@jmv'
        set_0 = {str_0, str_0, str_0, str_0}
        list_0 = [str_0]
        bytes_0 = b'n\x8e\r\xb5\xcaG\x0b.'
        action_module_0 = module_0.ActionModule(set_0, list_0, str_0, bytes_0, list_0, str_0)

if __name__ == "__main__":
    unittest.main()
