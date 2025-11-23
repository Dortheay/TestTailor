import unittest
import timeout_decorator
import ansible.executor.powershell.module_manifest as module_0

class Test_Module_manifest_2(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        try:
            p_s_module_dep_finder_0 = module_0.PSModuleDepFinder()
            int_0 = 939
            var_0 = p_s_module_dep_finder_0.scan_exec_script(int_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
