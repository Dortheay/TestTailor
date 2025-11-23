import unittest
import timeout_decorator
import ansible.playbook.included_file as module_0

class Test_Included_file_3(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        try:
            str_0 = 'test_file'
            var_0 = {}
            var_1 = {}
            var_2 = None
            included_file_0 = module_0.IncludedFile(str_0, var_0, var_1, var_2)
            str_1 = 'test_host'
            var_3 = included_file_0.add_host(str_1)
            var_4 = included_file_0.add_host(str_1)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
