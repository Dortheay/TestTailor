import unittest
import timeout_decorator
import ansible.parsing.dataloader as module_0

class Test_Dataloader_12(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_11(self):
        try:
            float_0 = None
            str_0 = '7'
            data_loader_0 = module_0.DataLoader()
            var_0 = data_loader_0.find_vars_files(float_0, str_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
