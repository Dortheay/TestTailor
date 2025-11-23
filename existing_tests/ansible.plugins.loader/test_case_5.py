import unittest
import timeout_decorator
import ansible.plugins.loader as module_0

class Test_Loader_6(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_5(self):
        try:
            str_0 = 'd,|~QP[y@{o3'
            var_0 = module_0.get_shell_plugin(str_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
