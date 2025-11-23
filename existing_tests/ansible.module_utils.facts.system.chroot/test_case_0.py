import unittest
import timeout_decorator
import ansible.module_utils.facts.system.chroot as module_0

class Test_Chroot_1(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        var_0 = module_0.is_chroot()

if __name__ == "__main__":
    unittest.main()
