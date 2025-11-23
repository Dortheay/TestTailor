import unittest
import timeout_decorator
import ansible.module_utils.facts.virtual.sysctl as module_0

class Test_Sysctl_3(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_2(self):
        try:
            virtual_sysctl_detection_mixin_0 = module_0.VirtualSysctlDetectionMixin()
            list_0 = []
            var_0 = virtual_sysctl_detection_mixin_0.detect_virt_vendor(list_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
