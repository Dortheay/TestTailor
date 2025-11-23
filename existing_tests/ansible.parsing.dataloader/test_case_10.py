import unittest
import timeout_decorator
import ansible.parsing.dataloader as module_0

class Test_Dataloader_11(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_10(self):
        try:
            data_loader_0 = module_0.DataLoader()
            var_0 = data_loader_0.cleanup_all_tmp_files()
            data_loader_1 = module_0.DataLoader()
            str_0 = "exampzM'e.j2"
            bool_0 = False
            var_1 = data_loader_1.path_dwim_relative(str_0, str_0, str_0, bool_0)
            float_0 = 4185.0
            str_1 = 'MiP.gpT NbYh?><'
            var_2 = data_loader_0.get_real_file(float_0, str_1)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
