import unittest
import timeout_decorator
import ansible.utils.display as module_0
import ansible.plugins.filter.mathstuff as module_1

class Test_Mathstuff_18(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_9(self):
        try:
            bytes_0 = b'\x81\x89\xd7\xa1E\x02\x0eE\r\xbb\xc0'
            var_0 = module_1.logarithm(bytes_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
