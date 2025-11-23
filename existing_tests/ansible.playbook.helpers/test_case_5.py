import unittest
import timeout_decorator
import ansible.playbook.helpers as module_0

class Test_Helpers_6(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_5(self):
        try:
            list_0 = []
            float_0 = 0.001
            var_0 = module_0.load_list_of_roles(list_0, float_0)
            float_1 = -2769.7353
            bytes_0 = b'\xd9\x96VV\xc5\x1e\xaf\xdf'
            tuple_0 = (float_1, bytes_0)
            str_0 = '(0Y*",:SVQh9L'
            complex_0 = None
            var_1 = module_0.load_list_of_blocks(tuple_0, str_0, complex_0, complex_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
