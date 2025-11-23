import unittest
import timeout_decorator
import ansible.inventory.host as module_0
import ansible.inventory.group as module_1

class Test_Host_3(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_2(self):
        try:
            int_0 = -4110
            str_0 = 'h\\L5kld'
            host_0 = module_0.Host(int_0, str_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
