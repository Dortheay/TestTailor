import unittest
import timeout_decorator
import ansible.executor.powershell.module_manifest as module_0

class Test_Module_manifest_6(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_3(self):
        bytes_0 = b'\x8e'
        str_0 = 'Ug'
        tuple_0 = ()
        p_s_module_dep_finder_0 = module_0.PSModuleDepFinder()
        var_0 = p_s_module_dep_finder_0.scan_module(bytes_0, str_0, tuple_0, tuple_0)
        p_s_module_dep_finder_1 = module_0.PSModuleDepFinder()

if __name__ == "__main__":
    unittest.main()
