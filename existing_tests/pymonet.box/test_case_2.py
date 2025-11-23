import unittest
import timeout_decorator
import builtins as module_0
import pymonet.box as module_1

class Test_Box_3(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_2(self):
        try:
            tuple_0 = ()
            float_0 = 1077.12
            str_0 = '\n        Transform Maybe into Validation.\n\n        :returns: successfull Validation monad with previous value or None when Maybe is empty\n        :rtype: Validation[A, []]\n        '
            box_0 = module_1.Box(str_0)
            var_0 = box_0.to_try()
            box_1 = module_1.Box(float_0)
            var_1 = box_1.bind(tuple_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
