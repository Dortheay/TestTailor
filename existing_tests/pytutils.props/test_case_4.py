import unittest
import timeout_decorator
import pytutils.props as module_0

class Test_Props_5(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        bool_0 = False
        var_0 = module_0.lazyperclassproperty(bool_0)

if __name__ == "__main__":
    unittest.main()
