import unittest
import timeout_decorator
import ansible.module_utils.facts.system.ssh_pub_keys as module_0

class Test_Ssh_pub_keys_2(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        ssh_pub_key_fact_collector_0 = module_0.SshPubKeyFactCollector()
        var_0 = ssh_pub_key_fact_collector_0.collect()

if __name__ == "__main__":
    unittest.main()
