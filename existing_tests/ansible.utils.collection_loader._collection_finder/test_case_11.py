import unittest
import timeout_decorator
import ansible.utils.collection_loader._collection_finder as module_0

class Test__collection_finder_12(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_3(self):
        try:
            str_0 = 'ansible.some_module'
            var_0 = None
            ansible_internal_redirect_loader_0 = module_0._AnsibleInternalRedirectLoader(str_0, var_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
