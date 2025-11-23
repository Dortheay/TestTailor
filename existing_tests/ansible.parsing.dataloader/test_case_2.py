import unittest
import timeout_decorator
import ansible.parsing.dataloader as module_0

class Test_Dataloader_3(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_2(self):
        try:
            str_0 = '*p4y~mWUeOf?\x0cFL\t'
            data_loader_0 = module_0.DataLoader()
            var_0 = data_loader_0.get_real_file(str_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
