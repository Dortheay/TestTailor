import unittest
import timeout_decorator
import ansible.plugins.loader as module_0

class Test_Loader_1(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        try:
            str_0 = 'T@\nRNv.j'
            dict_0 = {str_0: str_0, str_0: str_0}
            var_0 = module_0.add_all_plugin_dirs(dict_0)
            var_1 = module_0.get_shell_plugin()
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
