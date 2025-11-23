import unittest
import timeout_decorator
import httpie.plugins.base as module_0

class Test_Base_4(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        try:
            auth_plugin_0 = module_0.AuthPlugin()
            var_0 = auth_plugin_0.get_auth()
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
