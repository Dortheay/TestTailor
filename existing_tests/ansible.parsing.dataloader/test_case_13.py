import unittest
import timeout_decorator
import ansible.parsing.dataloader as module_0

class Test_Dataloader_14(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_13(self):
        try:
            data_loader_0 = module_0.DataLoader()
            str_0 = 'exa:ple.yml'
            var_0 = data_loader_0.path_dwim_relative_stack(str_0, str_0, str_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
