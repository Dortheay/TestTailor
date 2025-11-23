import unittest
import timeout_decorator
import ansible.executor.play_iterator as module_0

class Test_Play_iterator_3(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_2(self):
        bytes_0 = b'F\xa9\xef\x98\x81\xfc.v\x1fw\xa3\x1a\xab\x97S\xb4.'
        host_state_0 = module_0.HostState(bytes_0)
        var_0 = host_state_0.__str__()

if __name__ == "__main__":
    unittest.main()
