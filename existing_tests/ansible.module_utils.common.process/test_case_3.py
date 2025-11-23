import unittest
import timeout_decorator
import ansible.module_utils.common.process as module_0

class Test_Process_4(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_3(self):
        try:
            set_0 = None
            bool_0 = True
            str_0 = '2"\x0cc63|8'
            tuple_0 = (set_0, bool_0, bool_0, str_0)
            var_0 = module_0.get_bin_path(set_0, tuple_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
