import unittest
import timeout_decorator
import ansible.module_utils.facts.system.ssh_pub_keys as module_0

class Test_Ssh_pub_keys_1(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        ssh_pub_key_fact_collector_0 = module_0.SshPubKeyFactCollector()

if __name__ == "__main__":
    unittest.main()
