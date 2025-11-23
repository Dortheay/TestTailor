import unittest
import timeout_decorator
import ansible.modules.apt_repository as module_0

class Test_Apt_repository_3(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_2(self):
        try:
            int_0 = 302
            tuple_0 = (int_0,)
            ubuntu_sources_list_0 = module_0.UbuntuSourcesList(tuple_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
