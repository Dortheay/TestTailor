import unittest
import timeout_decorator
import sanic.helpers as module_0

class Test_Helpers_12(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_3(self):
        try:
            str_0 = '5!_.w{\t'
            var_0 = module_0.import_string(str_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
