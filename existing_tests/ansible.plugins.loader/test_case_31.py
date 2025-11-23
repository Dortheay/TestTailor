import unittest
import timeout_decorator
import ansible.plugins.loader as module_0

class Test_Loader_32(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_4(self):
        dict_0 = {}
        str_0 = '#wN}O42n9$":chdZ<'
        var_0 = module_0.get_shell_plugin(dict_0, str_0)

if __name__ == "__main__":
    unittest.main()
