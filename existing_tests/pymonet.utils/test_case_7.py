import unittest
import timeout_decorator
import pymonet.utils as module_0

class Test_Utils_8(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_2(self):
        str_0 = 'zSRiFqF\rp\\Wn'
        callable_0 = None
        tuple_0 = (str_0, callable_0)
        list_0 = [tuple_0, tuple_0]
        var_0 = module_0.cond(list_0)

if __name__ == "__main__":
    unittest.main()
