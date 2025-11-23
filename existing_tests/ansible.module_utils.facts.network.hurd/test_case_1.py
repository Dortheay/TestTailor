import unittest
import timeout_decorator
import ansible.module_utils.facts.network.hurd as module_0

class Test_Hurd_2(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        try:
            dict_0 = {}
            bytes_0 = b'xc\x1e\x1b\xb0\xf1\xf5\x8e\x7f\xf3}\xaa\t\xcf:\xf0;\xc3'
            hurd_network_collector_0 = module_0.HurdNetworkCollector()
            str_0 = ")V;{f'DqFG>;<T`"
            hurd_pfinet_network_0 = module_0.HurdPfinetNetwork(str_0)
            var_0 = hurd_pfinet_network_0.assign_network_facts(dict_0, bytes_0, hurd_network_collector_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
