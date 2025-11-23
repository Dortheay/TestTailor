import unittest
import timeout_decorator
import ansible.plugins.loader as module_0

class Test_Loader_3(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_2(self):
        try:
            int_0 = 3200
            var_0 = module_0.get_shell_plugin(int_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
