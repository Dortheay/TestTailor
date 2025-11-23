import unittest
import timeout_decorator
import ansible.modules.command as module_0

class Test_Command_2(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        str_0 = 'o?2[>a'
        var_0 = module_0.check_command(str_0, str_0)

if __name__ == "__main__":
    unittest.main()
