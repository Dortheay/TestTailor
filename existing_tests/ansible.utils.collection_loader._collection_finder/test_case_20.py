import unittest
import timeout_decorator
import ansible.utils.collection_loader._collection_finder as module_0

class Test__collection_finder_21(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_12(self):
        try:
            str_0 = 'Mu.{tQCvr1o|l!K?'
            list_0 = [str_0, str_0, str_0]
            ansible_internal_redirect_loader_0 = module_0._AnsibleInternalRedirectLoader(str_0, list_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
