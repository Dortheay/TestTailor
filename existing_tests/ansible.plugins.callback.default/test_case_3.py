import unittest
import timeout_decorator
import ansible.plugins.callback.default as module_0

class Test_Default_4(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        try:
            set_0 = set()
            callback_module_0 = module_0.CallbackModule()
            str_0 = 'WYTpS*x'
            str_1 = '}T8F%K+)y%C!f5UR'
            var_0 = callback_module_0.v2_playbook_on_notify(str_0, str_1)
            var_1 = callback_module_0.v2_playbook_on_no_hosts_matched()
            var_2 = callback_module_0.v2_runner_on_failed(set_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
