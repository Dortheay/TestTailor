import unittest
import timeout_decorator
import ansible.playbook.role.metadata as module_0

class Test_Metadata_4(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_3(self):
        try:
            float_0 = -276.84
            bytes_0 = b'?\x1d0\xbeR='
            bytes_1 = b'\xe1'
            role_metadata_0 = module_0.RoleMetadata()
            var_0 = role_metadata_0.serialize()
            dict_0 = {}
            str_0 = 't1EZ'
            var_1 = role_metadata_0.load(dict_0, str_0, dict_0)
            var_2 = role_metadata_0.serialize()
            list_0 = [bytes_0]
            role_metadata_1 = module_0.RoleMetadata(list_0)
            role_metadata_2 = module_0.RoleMetadata(bytes_1)
            list_1 = []
            role_metadata_3 = module_0.RoleMetadata(list_1)
            str_1 = 'WfCS`=LXIRd+;w(w*H\x0by'
            str_2 = ')]@gf!tsJvN>Y;mgNIo'
            var_3 = role_metadata_0.load(float_0, str_1, str_1, str_2)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
