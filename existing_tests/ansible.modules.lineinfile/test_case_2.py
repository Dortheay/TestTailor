import unittest
import timeout_decorator
import ansible.modules.lineinfile as module_0

class Test_Lineinfile_3(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        try:
            int_0 = -4371
            set_0 = {int_0, int_0, int_0}
            int_1 = -1984
            var_0 = module_0.check_file_attrs(int_0, set_0, int_1, int_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
