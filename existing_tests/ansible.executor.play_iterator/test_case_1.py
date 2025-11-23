import unittest
import timeout_decorator
import ansible.executor.play_iterator as module_0

class Test_Play_iterator_2(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        str_0 = 'hB<\\-l`By\x0c'
        host_state_0 = module_0.HostState(str_0)
        var_0 = host_state_0.copy()
        var_1 = host_state_0.__eq__(host_state_0)
        var_2 = host_state_0.copy()
        var_3 = host_state_0.__repr__()

if __name__ == "__main__":
    unittest.main()
