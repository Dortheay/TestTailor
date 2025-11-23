import unittest
import timeout_decorator
import isort.exceptions as module_0
import builtins as module_1
import pathlib as module_2

class Test_Exceptions_1(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        str_0 = ''
        profile_does_not_exist_0 = module_0.ProfileDoesNotExist(str_0)

if __name__ == "__main__":
    unittest.main()
