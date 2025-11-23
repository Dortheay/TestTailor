import unittest
import timeout_decorator
import ansible.module_utils.facts.utils as module_0

class Test_Utils_3(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_2(self):
        try:
            float_0 = -1167.014375
            var_0 = module_0.get_mount_size(float_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
