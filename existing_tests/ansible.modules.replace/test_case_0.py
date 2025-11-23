import unittest
import timeout_decorator
import ansible.modules.replace as module_0

class Test_Replace_1(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        try:
            int_0 = 200000
            float_0 = -1.2
            list_0 = None
            var_0 = module_0.write_changes(int_0, float_0, list_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
