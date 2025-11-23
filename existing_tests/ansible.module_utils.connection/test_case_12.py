import unittest
import timeout_decorator
import ansible.module_utils.connection as module_0

class Test_Connection_13(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_12(self):
        try:
            bool_0 = True
            connection_0 = module_0.Connection(bool_0)
            var_0 = module_0.recv_data(connection_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
