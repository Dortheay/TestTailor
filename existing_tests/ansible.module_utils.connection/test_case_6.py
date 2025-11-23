import unittest
import timeout_decorator
import ansible.module_utils.connection as module_0

class Test_Connection_7(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_6(self):
        try:
            connection_error_0 = None
            connection_0 = module_0.Connection(connection_error_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
