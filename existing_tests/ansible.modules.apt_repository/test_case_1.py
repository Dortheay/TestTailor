import unittest
import timeout_decorator
import ansible.modules.apt_repository as module_0

class Test_Apt_repository_2(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        try:
            str_0 = 'object'
            sources_list_0 = module_0.SourcesList(str_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
