import unittest
import timeout_decorator
import ansible.parsing.dataloader as module_0

class Test_Dataloader_6(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_5(self):
        try:
            bytes_0 = b'~'
            data_loader_0 = module_0.DataLoader()
            var_0 = data_loader_0.load_from_file(bytes_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
