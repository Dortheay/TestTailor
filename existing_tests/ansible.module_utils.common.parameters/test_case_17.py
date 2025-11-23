import unittest
import timeout_decorator
import ansible.module_utils.common.parameters as module_0

class Test_Parameters_18(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_4(self):
        try:
            bytes_0 = b'\x92\xc0K\xadW<\xd9\\\xd9\x1c\xe68\xc0\xe5xFW{\xd0'
            float_0 = None
            var_0 = module_0.remove_values(bytes_0, float_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
