import unittest
import timeout_decorator
import ansible.parsing.dataloader as module_0

class Test_Dataloader_13(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_12(self):
        try:
            float_0 = 645.1310571596215
            set_0 = None
            data_loader_0 = module_0.DataLoader()
            var_0 = data_loader_0.cleanup_tmp_file(set_0)
            data_loader_1 = module_0.DataLoader()
            complex_0 = None
            var_1 = data_loader_1.set_basedir(complex_0)
            var_2 = data_loader_1.is_executable(float_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
