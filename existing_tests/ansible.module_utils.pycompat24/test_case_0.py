import unittest
import timeout_decorator
import ansible.module_utils.pycompat24 as module_0

class Test_Pycompat24_1(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        var_0 = module_0.get_exception()

if __name__ == "__main__":
    unittest.main()
