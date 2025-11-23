import unittest
import timeout_decorator
import ansible.parsing.dataloader as module_0

class Test_Dataloader_7(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_6(self):
        try:
            bytes_0 = b'\xd3\x92\xc5?f\xf4T\xab\xf0'
            float_0 = 676.7
            dict_0 = {float_0: float_0}
            data_loader_0 = module_0.DataLoader()
            var_0 = data_loader_0.path_dwim_relative(bytes_0, float_0, dict_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
