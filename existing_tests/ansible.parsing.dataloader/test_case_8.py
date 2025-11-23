import unittest
import timeout_decorator
import ansible.parsing.dataloader as module_0

class Test_Dataloader_9(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_8(self):
        try:
            str_0 = None
            list_0 = [str_0, str_0, str_0, str_0]
            bytes_0 = b'\xbf\xd1\xac\x8ar\xc3Fd\xb5f#'
            bool_0 = False
            data_loader_0 = module_0.DataLoader()
            var_0 = data_loader_0.path_dwim_relative_stack(list_0, bytes_0, bool_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
