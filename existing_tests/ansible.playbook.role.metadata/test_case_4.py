import unittest
import timeout_decorator
import ansible.playbook.role.metadata as module_0

class Test_Metadata_5(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        role_metadata_0 = module_0.RoleMetadata()

if __name__ == "__main__":
    unittest.main()
