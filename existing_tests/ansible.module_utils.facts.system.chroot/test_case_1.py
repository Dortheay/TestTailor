import unittest
import timeout_decorator
import ansible.module_utils.facts.system.chroot as module_0

class Test_Chroot_2(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        bool_0 = False
        chroot_fact_collector_0 = module_0.ChrootFactCollector(bool_0)
        var_0 = chroot_fact_collector_0.collect()

if __name__ == "__main__":
    unittest.main()
