import unittest
import timeout_decorator
import pytutils.lazy.simple_import as module_0

class Test_Simple_import_3(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_2(self):
        bool_0 = True
        var_0 = module_0.make_lazy(bool_0)

if __name__ == "__main__":
    unittest.main()
