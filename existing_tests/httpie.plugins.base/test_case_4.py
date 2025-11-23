import unittest
import timeout_decorator
import httpie.plugins.base as module_0

class Test_Base_5(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_2(self):
        try:
            transport_plugin_0 = module_0.TransportPlugin()
            var_0 = transport_plugin_0.get_adapter()
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
