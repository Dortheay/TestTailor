import unittest
import timeout_decorator
import ansible.vars.manager as module_0

class Test_Manager_2(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        try:
            bytes_0 = b'\x81!\xa1\x05'
            var_0 = module_0.preprocess_vars(bytes_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
