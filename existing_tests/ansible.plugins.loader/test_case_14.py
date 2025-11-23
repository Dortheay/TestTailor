import unittest
import timeout_decorator
import ansible.plugins.loader as module_0

class Test_Loader_15(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_14(self):
        try:
            str_0 = '/data/zhuxx/TIARA-study/codamosa/test-apps/ansible/lib/ansible/plugins/doc_fragments/windows'
            plugin_load_context_0 = module_0.PluginLoadContext()
            var_0 = plugin_load_context_0.redirect(str_0)
            str_1 = 'd,|~QP[y@{o3'
            var_1 = module_0.get_shell_plugin(str_1)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
