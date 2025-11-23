import unittest
import timeout_decorator
import ansible.module_utils.facts.ansible_collector as module_0

class Test_Ansible_collector_8(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        try:
            bool_0 = False
            set_0 = {bool_0, bool_0, bool_0, bool_0}
            float_0 = 0.1
            var_0 = module_0.get_ansible_collector(set_0, float_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
