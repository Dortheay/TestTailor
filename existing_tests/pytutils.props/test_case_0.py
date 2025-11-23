import unittest
import timeout_decorator
import pytutils.props as module_0

class Test_Props_1(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        try:
            int_0 = 1360
            var_0 = module_0.lazyperclassproperty(int_0)
            float_0 = -1091.57
            int_1 = 600
            set_0 = {float_0, float_0, int_1, int_1}
            roclassproperty_0 = module_0.roclassproperty(set_0)
            bytes_0 = b'9\xa9\x0e&\xa4\x00\xe6\xfeW\xad\xca`\xe8II'
            var_1 = roclassproperty_0.__get__(bytes_0, roclassproperty_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
