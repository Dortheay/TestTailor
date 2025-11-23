import unittest
import timeout_decorator
import ansible.config.manager as module_0

class Test_Manager_5(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_4(self):
        try:
            tuple_0 = ()
            config_manager_0 = module_0.ConfigManager(tuple_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
