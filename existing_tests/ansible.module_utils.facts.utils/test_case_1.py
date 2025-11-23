import unittest
import timeout_decorator
import ansible.module_utils.facts.utils as module_0

class Test_Utils_2(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        try:
            bool_0 = True
            var_0 = module_0.get_mount_size(bool_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
