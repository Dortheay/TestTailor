import unittest
import timeout_decorator
import ansible.parsing.dataloader as module_0

class Test_Dataloader_29(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_10(self):
        data_loader_0 = module_0.DataLoader()
        bool_0 = True
        str_0 = 'valid_eSdir'
        str_1 = '.yml'
        str_2 = [str_1, str_1]
        var_0 = data_loader_0.find_vars_files(str_0, str_0, str_2, bool_0)

if __name__ == "__main__":
    unittest.main()
