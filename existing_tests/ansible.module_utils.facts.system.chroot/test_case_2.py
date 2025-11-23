import unittest
import timeout_decorator
import ansible.module_utils.facts.system.chroot as module_0

class Test_Chroot_3(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        try:
            chroot_fact_collector_0 = module_0.ChrootFactCollector()
            var_0 = chroot_fact_collector_0.collect()
            var_1 = module_0.is_chroot(chroot_fact_collector_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
