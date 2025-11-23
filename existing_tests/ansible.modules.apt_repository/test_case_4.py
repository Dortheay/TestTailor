import unittest
import timeout_decorator
import ansible.modules.apt_repository as module_0

class Test_Apt_repository_5(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_4(self):
        try:
            bytes_0 = b'\xe8\xccEhj\xea\x7fdi#q6\x8d\xc2'
            sources_list_0 = None
            str_0 = 'isgid'
            var_0 = module_0.revert_sources_list(bytes_0, sources_list_0, str_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
