import unittest
import timeout_decorator
import thefuck.types as module_0

class Test_Types_6(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        str_0 = ''
        bool_0 = False
        command_0 = module_0.Command(str_0, bool_0)

if __name__ == "__main__":
    unittest.main()
