import unittest
import timeout_decorator
import ansible.module_utils.facts.virtual.linux as module_0

class Test_Linux_2(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        bytes_0 = b'qw\xe3E\xa3\xa6\xfe\x99\x80?\xc3\x03\x1dE\xe3\x17\xd1'
        linux_virtual_collector_0 = module_0.LinuxVirtualCollector(bytes_0)

if __name__ == "__main__":
    unittest.main()
