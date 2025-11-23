import unittest
import timeout_decorator
import ansible.parsing.dataloader as module_0

class Test_Dataloader_19(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        data_loader_0 = module_0.DataLoader()

if __name__ == "__main__":
    unittest.main()
