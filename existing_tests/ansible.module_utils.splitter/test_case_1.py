import unittest
import timeout_decorator
import ansible.module_utils.splitter as module_0

class Test_Splitter_2(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        try:
            bytes_0 = b'\x952\xcc\x9c\xf6'
            var_0 = module_0.split_args(bytes_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
