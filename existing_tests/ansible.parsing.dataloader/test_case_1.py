import unittest
import timeout_decorator
import ansible.parsing.dataloader as module_0

class Test_Dataloader_2(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        try:
            str_0 = 'I0pRV<:'
            int_0 = 594
            data_loader_0 = module_0.DataLoader()
            data_loader_1 = module_0.DataLoader()
            var_0 = data_loader_1.load_from_file(str_0, int_0, data_loader_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
