import unittest
import timeout_decorator
import thefuck.rules.cp_create_destination as module_0

class Test_Cp_create_destination_1(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        try:
            list_0 = []
            var_0 = module_0.match(list_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
