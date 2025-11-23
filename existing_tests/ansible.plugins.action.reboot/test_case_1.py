import unittest
import timeout_decorator
import ansible.plugins.action.reboot as module_0

class Test_Reboot_2(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        timed_out_exception_0 = module_0.TimedOutException()

if __name__ == "__main__":
    unittest.main()
