import unittest
import timeout_decorator
import ansible.parsing.dataloader as module_0

class Test_Dataloader_18(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_17(self):
        try:
            data_loader_0 = module_0.DataLoader()
            bytes_0 = b''
            var_0 = data_loader_0.set_basedir(bytes_0)
            str_0 = '/mock/path'
            str_1 = 'vars'
            str_2 = '.yml'
            str_3 = [str_2, str_1]
            var_1 = data_loader_0.find_vars_files(str_0, str_1, str_3)
            float_0 = 3271.51
            tuple_0 = (str_0, data_loader_0, float_0)
            data_loader_1 = module_0.DataLoader()
            var_2 = data_loader_0.get_real_file(tuple_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
