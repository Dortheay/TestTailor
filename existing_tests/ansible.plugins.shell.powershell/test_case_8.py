import unittest
import timeout_decorator
import ansible.plugins.shell.powershell as module_0

class Test_Powershell_9(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_8(self):
        shell_module_0 = module_0.ShellModule()
        str_0 = "$env:TEST_VAR='test_value';"
        str_1 = '#!powershell'
        str_2 = 'test_script'
        var_0 = None
        int_0 = 3763
        tuple_0 = (int_0, shell_module_0)
        var_1 = shell_module_0.expand_user(tuple_0)
        var_2 = shell_module_0.build_module_command(str_0, str_1, str_2, var_0)
        float_0 = 286.388
        list_0 = [int_0, var_1, float_0, tuple_0]
        var_3 = shell_module_0.expand_user(list_0)
        shell_module_1 = module_0.ShellModule()
        dict_0 = None
        dict_1 = {str_2: int_0}
        var_4 = shell_module_1.mkdtemp(dict_0, dict_1, dict_0, tuple_0)
        shell_module_2 = module_0.ShellModule()
        var_5 = shell_module_2.remove(dict_0)
        list_1 = [var_1, int_0, var_3, str_2]
        var_6 = shell_module_2.join_path(*list_1)

if __name__ == "__main__":
    unittest.main()
