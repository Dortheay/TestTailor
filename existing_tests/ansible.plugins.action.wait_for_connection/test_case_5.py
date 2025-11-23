import unittest
import timeout_decorator
import ansible.plugins.action.wait_for_connection as module_0

class Test_Wait_for_connection_6(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        float_0 = 1.5
        list_0 = [float_0, float_0]
        timed_out_exception_0 = module_0.TimedOutException(*list_0)

if __name__ == "__main__":
    unittest.main()
