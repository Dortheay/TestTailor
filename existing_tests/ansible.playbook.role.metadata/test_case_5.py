import unittest
import timeout_decorator
import ansible.playbook.role.metadata as module_0

class Test_Metadata_6(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        role_metadata_0 = module_0.RoleMetadata()
        var_0 = role_metadata_0.serialize()
        role_metadata_1 = module_0.RoleMetadata()

if __name__ == "__main__":
    unittest.main()
