import unittest
import timeout_decorator
import ansible.parsing.dataloader as module_0

class Test_Dataloader_4(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_3(self):
        try:
            dict_0 = None
            bytes_0 = b'\x04\x1ffE\x8c\xe3d^+\x18\xd65'
            bytes_1 = b'\xd9\x8a\xfermp\x1c\xe3\xc7\x0b\xb3\x08 \x18)Gh'
            list_0 = [dict_0]
            data_loader_0 = module_0.DataLoader()
            var_0 = data_loader_0.set_vault_secrets(list_0)
            list_1 = [bytes_0, bytes_0, bytes_1]
            data_loader_1 = module_0.DataLoader()
            var_1 = data_loader_1.get_basedir()
            data_loader_2 = module_0.DataLoader()
            var_2 = data_loader_0.get_basedir()
            var_3 = data_loader_2.cleanup_all_tmp_files()
            var_4 = data_loader_2.list_directory(list_1)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
