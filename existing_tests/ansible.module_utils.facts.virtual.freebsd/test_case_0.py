import unittest
import timeout_decorator
import ansible.module_utils.facts.virtual.freebsd as module_0

class Test_Freebsd_1(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        try:
            str_0 = 'd'
            free_b_s_d_virtual_0 = module_0.FreeBSDVirtual(str_0)
            var_0 = free_b_s_d_virtual_0.get_virtual_facts()
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
