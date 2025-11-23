import unittest
import timeout_decorator
import ansible.parsing.dataloader as module_0

class Test_Dataloader_24(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_5(self):
        str_0 = 'R9Ob'
        data_loader_0 = module_0.DataLoader()
        var_0 = data_loader_0.cleanup_tmp_file(str_0)

if __name__ == "__main__":
    unittest.main()
