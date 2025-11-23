import unittest
import timeout_decorator
import ansible.module_utils.facts.virtual.linux as module_0

class Test_Linux_1(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        try:
            list_0 = []
            linux_virtual_0 = module_0.LinuxVirtual(list_0)
            var_0 = linux_virtual_0.get_virtual_facts()
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
