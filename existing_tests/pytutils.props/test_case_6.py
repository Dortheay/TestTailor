import unittest
import timeout_decorator
import pytutils.props as module_0

class Test_Props_7(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_3(self):
        bool_0 = True
        var_0 = module_0.lazyperclassproperty(bool_0)
        tuple_0 = None
        var_1 = module_0.lazyperclassproperty(tuple_0)
        str_0 = 'rTW&*kC'
        roclassproperty_0 = module_0.roclassproperty(str_0)
        list_0 = [var_1, bool_0, bool_0, bool_0]
        setterproperty_0 = module_0.setterproperty(roclassproperty_0, list_0)
        var_2 = module_0.lazyperclassproperty(setterproperty_0)

if __name__ == "__main__":
    unittest.main()
