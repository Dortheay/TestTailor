import unittest
import timeout_decorator
import ansible.plugins.loader as module_0

class Test_Loader_26(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_25(self):
        try:
            str_0 = 'IomPsRWXc'
            var_0 = module_0.get_shell_plugin(str_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
