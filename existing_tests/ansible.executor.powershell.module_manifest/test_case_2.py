import unittest
import timeout_decorator
import ansible.executor.powershell.module_manifest as module_0

class Test_Module_manifest_3(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        p_s_module_dep_finder_0 = module_0.PSModuleDepFinder()

if __name__ == "__main__":
    unittest.main()
