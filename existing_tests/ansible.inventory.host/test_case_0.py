import unittest
import timeout_decorator
import ansible.inventory.host as module_0
import ansible.inventory.group as module_1

class Test_Host_1(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        try:
            str_0 = '(9*xWN'
            host_0 = module_0.Host()
            float_0 = 894.6676
            var_0 = host_0.get_groups()
            var_1 = host_0.__eq__(str_0)
            var_2 = host_0.__hash__()
            var_3 = host_0.__setstate__(float_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
