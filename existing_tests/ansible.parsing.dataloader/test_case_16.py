import unittest
import timeout_decorator
import ansible.parsing.dataloader as module_0

class Test_Dataloader_17(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_16(self):
        try:
            data_loader_0 = module_0.DataLoader()
            bytes_0 = b'\x0f\xdc<\xd6\xbc\xd5p1\xfcW\xbb\xcc'
            tuple_0 = ()
            var_0 = data_loader_0.load_from_file(bytes_0, tuple_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
