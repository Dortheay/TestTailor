import unittest
import timeout_decorator
import sanic.helpers as module_0

class Test_Helpers_5(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_4(self):
        str_0 = 'types.SimpleNamespace'
        var_0 = module_0.import_string(str_0)

if __name__ == "__main__":
    unittest.main()
