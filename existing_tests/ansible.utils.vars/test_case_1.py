import unittest
import timeout_decorator
import ansible.utils.vars as module_0

class Test_Vars_2(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        bytes_0 = b'S;%o\xf8~\xa2\x0b\xe3 af\xba'
        var_0 = module_0.load_extra_vars(bytes_0)

if __name__ == "__main__":
    unittest.main()
