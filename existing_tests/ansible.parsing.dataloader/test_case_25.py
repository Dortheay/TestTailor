import unittest
import timeout_decorator
import ansible.parsing.dataloader as module_0

class Test_Dataloader_26(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_7(self):
        data_loader_0 = module_0.DataLoader()
        str_0 = '/fake/path'
        str_1 = 'templates'
        str_2 = 'example.j2'
        bool_0 = False
        var_0 = data_loader_0.path_dwim_relative(str_0, str_1, str_2, bool_0)

if __name__ == "__main__":
    unittest.main()
