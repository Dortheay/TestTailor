import unittest
import timeout_decorator
import ansible.modules.dnf as module_0

class Test_Dnf_1(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        try:
            int_0 = -4048
            dnf_module_0 = module_0.DnfModule(int_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
