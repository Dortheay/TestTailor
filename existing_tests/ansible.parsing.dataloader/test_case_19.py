import unittest
import timeout_decorator
import ansible.parsing.dataloader as module_0

class Test_Dataloader_20(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        str_0 = '\nF\n"~n;\\(N\nEP'
        data_loader_0 = module_0.DataLoader()
        var_0 = data_loader_0.is_file(str_0)

if __name__ == "__main__":
    unittest.main()
