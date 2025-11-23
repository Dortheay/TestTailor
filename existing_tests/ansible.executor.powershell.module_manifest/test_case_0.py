import unittest
import timeout_decorator
import ansible.executor.powershell.module_manifest as module_0

class Test_Module_manifest_1(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        try:
            bool_0 = True
            p_s_module_dep_finder_0 = module_0.PSModuleDepFinder()
            p_s_module_dep_finder_1 = module_0.PSModuleDepFinder()
            var_0 = p_s_module_dep_finder_1.scan_module(bool_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
