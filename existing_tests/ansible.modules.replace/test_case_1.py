import unittest
import timeout_decorator
import ansible.modules.replace as module_0

class Test_Replace_2(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        try:
            tuple_0 = ()
            bool_0 = False
            float_0 = None
            var_0 = module_0.check_file_attrs(tuple_0, bool_0, float_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
