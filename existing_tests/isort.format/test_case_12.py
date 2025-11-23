import unittest
import timeout_decorator
import isort.format as module_0
import pathlib as module_1
import typing as module_2

class Test_Format_13(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        try:
            str_0 = '~Nj`n#6AO\n'
            bool_0 = module_0.ask_whether_to_apply_changes_to_file(str_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
