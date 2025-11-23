import unittest
import timeout_decorator
import ansible.executor.play_iterator as module_0

class Test_Play_iterator_5(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_4(self):
        str_0 = 'hB<\\-l`By\x0c'
        host_state_0 = module_0.HostState(str_0)
        var_0 = host_state_0.__str__()
        var_1 = host_state_0.get_current_block()
        var_2 = host_state_0.copy()
        bytes_0 = b'\xfa\x89\xf7\xd1\x06Y\x97\x92\xc5\x8e\xa4\x89\x04\xc5:\x86\xcbI'
        var_3 = host_state_0.__eq__(bytes_0)
        var_4 = host_state_0.__repr__()
        var_5 = host_state_0.get_current_block()

if __name__ == "__main__":
    unittest.main()
