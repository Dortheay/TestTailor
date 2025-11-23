import unittest
import timeout_decorator
import ansible.executor.powershell.module_manifest as module_0

class Test_Module_manifest_4(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        bytes_0 = b'\xa1&\xf4\x89\x01\xe0\xfd\xc5\x10\xa8\xa7a\x937R0t'
        str_0 = 'q@d\x0b|zk20.H>'
        p_s_module_dep_finder_0 = module_0.PSModuleDepFinder()
        var_0 = p_s_module_dep_finder_0.scan_module(bytes_0, str_0, str_0)

if __name__ == "__main__":
    unittest.main()
