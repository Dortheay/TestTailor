import unittest
import timeout_decorator
import thefuck.rules.cp_create_destination as module_0

class Test_Cp_create_destination_2(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        try:
            str_0 = '\\f\x0cv\x0b8cps:"<*\\L'
            var_0 = module_0.get_new_command(str_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
