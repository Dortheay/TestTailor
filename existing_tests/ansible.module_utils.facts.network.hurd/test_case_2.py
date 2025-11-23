import unittest
import timeout_decorator
import ansible.module_utils.facts.network.hurd as module_0

class Test_Hurd_3(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        try:
            str_0 = '{>Z}+Za@}5'
            hurd_pfinet_network_0 = module_0.HurdPfinetNetwork(str_0)
            var_0 = hurd_pfinet_network_0.populate()
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
