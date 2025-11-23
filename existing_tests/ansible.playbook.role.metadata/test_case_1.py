import unittest
import timeout_decorator
import ansible.playbook.role.metadata as module_0

class Test_Metadata_2(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        try:
            role_metadata_0 = module_0.RoleMetadata()
            str_0 = 'PSRP PUT %s to %s (offset=%d, size=%d'
            int_0 = 604800
            dict_0 = {role_metadata_0: str_0, str_0: int_0}
            var_0 = role_metadata_0.load(str_0, dict_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
