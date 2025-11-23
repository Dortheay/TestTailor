import unittest
import timeout_decorator
import ansible.plugins.loader as module_0

class Test_Loader_25(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_24(self):
        try:
            int_0 = 3215
            list_0 = None
            float_0 = 2019.46
            bool_0 = False
            str_0 = '/data/zhuxx/TIARA-study/codamosa/test-apps/ansible/lib/ansible/plugins/doc_fragments/__pycache__/windows'
            dict_0 = {float_0: int_0, int_0: float_0, int_0: bool_0}
            plugin_loader_0 = module_0.PluginLoader(float_0, bool_0, str_0, dict_0)
            var_0 = plugin_loader_0.get_with_context(list_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
