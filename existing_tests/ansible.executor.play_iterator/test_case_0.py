import unittest
import timeout_decorator
import ansible.executor.play_iterator as module_0

class Test_Play_iterator_1(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        bytes_0 = b'\xae\x9b\xa5\xab\x1f\xda\xe3'
        list_0 = [bytes_0]
        host_state_0 = module_0.HostState(list_0)

if __name__ == "__main__":
    unittest.main()
