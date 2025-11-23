import unittest
import timeout_decorator
import ansible.utils.collection_loader._collection_finder as module_0

class Test__collection_finder_3(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_2(self):
        int_0 = 1
        bytes_0 = b'\x88(n5 \x01Pb'
        ansible_path_hook_finder_0 = module_0._AnsiblePathHookFinder(int_0, bytes_0)

if __name__ == "__main__":
    unittest.main()
