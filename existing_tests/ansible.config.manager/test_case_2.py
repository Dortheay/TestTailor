import unittest
import timeout_decorator
import ansible.config.manager as module_0

class Test_Manager_3(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_2(self):
        try:
            str_0 = 'Bm~2>{"_'
            var_0 = module_0.get_config_type(str_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
