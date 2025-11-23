import unittest
import timeout_decorator
import ansible.playbook.role.metadata as module_0

class Test_Metadata_3(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_2(self):
        try:
            str_0 = '0;33'
            role_metadata_0 = module_0.RoleMetadata()
            var_0 = role_metadata_0.deserialize(str_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
