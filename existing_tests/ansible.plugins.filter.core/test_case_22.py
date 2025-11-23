import unittest
import timeout_decorator
import ansible.plugins.filter.core as module_0

class Test_Core_23(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_22(self):
        try:
            int_0 = 2615
            tuple_0 = (int_0,)
            list_0 = [tuple_0, int_0]
            list_1 = [list_0, int_0, tuple_0, tuple_0]
            var_0 = module_0.rand(list_1, int_0, int_0, int_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
