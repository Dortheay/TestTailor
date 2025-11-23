import unittest
import timeout_decorator
import ansible.playbook.role.metadata as module_0

class Test_Metadata_7(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_2(self):
        tuple_0 = None
        role_metadata_0 = module_0.RoleMetadata(tuple_0)
        str_0 = '~3z'
        dict_0 = {tuple_0: tuple_0, role_metadata_0: role_metadata_0, tuple_0: role_metadata_0, str_0: role_metadata_0}
        var_0 = role_metadata_0.deserialize(dict_0)

if __name__ == "__main__":
    unittest.main()
