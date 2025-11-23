import unittest
import timeout_decorator
import ansible.parsing.dataloader as module_0

class Test_Dataloader_1(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        try:
            float_0 = 1888.0
            str_0 = 'my[t\x0b!RLme%qj{b>iXl'
            str_1 = 'stdout chunk (state=%s):\n>>>%s<<<\n'
            data_loader_0 = module_0.DataLoader()
            var_0 = data_loader_0.find_vars_files(str_0, str_1)
            data_loader_1 = module_0.DataLoader()
            bytes_0 = b'\x18\x8c1\xd76\xebs\xadS\xcd\xaa/\x88n\xdbz\xc2'
            var_1 = data_loader_1.load(bytes_0, float_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
