import unittest
import timeout_decorator
import thefuck.rules.sudo_command_from_user_path

class Test_Sudo_command_from_user_path_2(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        pass

if __name__ == "__main__":
    unittest.main()
