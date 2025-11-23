import unittest
import timeout_decorator
import ansible.parsing.dataloader as module_0

class Test_Dataloader_15(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_14(self):
        try:
            list_0 = None
            dict_0 = {list_0: list_0}
            data_loader_0 = module_0.DataLoader()
            var_0 = data_loader_0.path_exists(dict_0)
            data_loader_1 = module_0.DataLoader()
            var_1 = data_loader_1.get_basedir()
            data_loader_2 = module_0.DataLoader()
            var_2 = data_loader_2.get_real_file(list_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
