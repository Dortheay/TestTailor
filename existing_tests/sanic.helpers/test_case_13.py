import unittest
import timeout_decorator
import sanic.helpers as module_0

class Test_Helpers_14(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_5(self):
        try:
            str_0 = 'os.path'
            var_0 = module_0.import_string(str_0)
            str_1 = 'module_name.ClassName'
            var_1 = module_0.import_string(str_1)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
