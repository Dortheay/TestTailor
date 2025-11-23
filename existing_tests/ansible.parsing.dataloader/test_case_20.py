import unittest
import timeout_decorator
import ansible.parsing.dataloader as module_0

class Test_Dataloader_21(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_2(self):
        data_loader_0 = module_0.DataLoader()
        str_0 = '/fake/path'
        bool_0 = False
        set_0 = set()
        var_0 = data_loader_0.is_directory(set_0)
        var_1 = data_loader_0.path_dwim_relative(str_0, str_0, str_0, bool_0)

if __name__ == "__main__":
    unittest.main()
