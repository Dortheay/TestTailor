import unittest
import timeout_decorator
import ansible.modules.apt_repository as module_0

class Test_Apt_repository_7(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        var_0 = module_0.main()
        int_0 = -773
        bool_0 = False
        list_0 = [var_0, var_0, var_0, var_0]
        sources_list_0 = module_0.SourcesList(list_0)
        var_1 = sources_list_0.modify(int_0, bool_0)

if __name__ == "__main__":
    unittest.main()
