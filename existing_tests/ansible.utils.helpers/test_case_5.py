import unittest
import timeout_decorator
import ansible.utils.helpers as module_0

class Test_Helpers_6(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        float_0 = None
        var_0 = module_0.object_to_dict(float_0)

if __name__ == "__main__":
    unittest.main()
