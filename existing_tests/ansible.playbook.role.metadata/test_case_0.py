import unittest
import timeout_decorator
import ansible.playbook.role.metadata as module_0

class Test_Metadata_1(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        try:
            str_0 = '<"mSYn'
            float_0 = 1705.0
            role_metadata_0 = module_0.RoleMetadata()
            dict_0 = {float_0: float_0}
            list_0 = [str_0]
            complex_0 = None
            bytes_0 = b'\x82\xa8\xe7\x03\xa6)\xa5\x87*\n\xd2'
            float_1 = 3091.739653
            tuple_0 = (list_0, complex_0, bytes_0, float_1)
            var_0 = role_metadata_0.load(dict_0, tuple_0, role_metadata_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
