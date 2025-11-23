import unittest
import timeout_decorator
import ansible.parsing.dataloader as module_0

class Test_Dataloader_25(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_6(self):
        data_loader_0 = module_0.DataLoader()
        data_loader_1 = module_0.DataLoader()
        var_0 = data_loader_1.set_basedir(data_loader_0)
        var_1 = data_loader_1.cleanup_all_tmp_files()

if __name__ == "__main__":
    unittest.main()
