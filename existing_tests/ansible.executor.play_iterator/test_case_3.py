import unittest
import timeout_decorator
import ansible.executor.play_iterator as module_0

class Test_Play_iterator_4(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_3(self):
        str_0 = '3HB^|'
        host_state_0 = module_0.HostState(str_0)
        var_0 = host_state_0.__eq__(str_0)

if __name__ == "__main__":
    unittest.main()
