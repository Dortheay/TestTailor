import unittest
import timeout_decorator
import ansible.parsing.dataloader as module_0

class Test_Dataloader_8(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_7(self):
        try:
            complex_0 = None
            dict_0 = {complex_0: complex_0}
            data_loader_0 = module_0.DataLoader()
            var_0 = data_loader_0.path_dwim_relative_stack(complex_0, dict_0, complex_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
