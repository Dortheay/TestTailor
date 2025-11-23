import unittest
import timeout_decorator
import ansible.executor.powershell.module_manifest as module_0

class Test_Module_manifest_5(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_2(self):
        p_s_module_dep_finder_0 = module_0.PSModuleDepFinder()
        bytes_0 = b'\n        #Requires -Module Ansible.ModuleUtils.TestModule\n        #AnsibleRequires -Powershell ansible_collections.test_namespace.test_collection.plugins.module_utils.test_util\n        #AnsibleRequires -CSharpUtil Ansible.TestUtil\n        #requires -version 5.1\n        #AnsibleRequires -osversion 10.0\n        #AnsibleRequires -become\n    '
        str_0 = 'test.namespace.module'
        bool_0 = False
        bool_1 = True
        var_0 = p_s_module_dep_finder_0.scan_module(bytes_0, str_0, bool_0, bool_1)

if __name__ == "__main__":
    unittest.main()
