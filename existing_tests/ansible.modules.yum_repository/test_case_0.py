import unittest
import timeout_decorator
import ansible.modules.yum_repository as module_0

class Test_Yum_repository_1(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        try:
            int_0 = -92
            yum_repo_0 = module_0.YumRepo(int_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
