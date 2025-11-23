import unittest
import timeout_decorator
import thefuck.entrypoints.fix_command

class Test_Fix_command_3(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        pass

if __name__ == "__main__":
    unittest.main()
