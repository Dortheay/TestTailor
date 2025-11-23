import unittest
import timeout_decorator
import ansible.module_utils.connection as module_0

class Test_Connection_14(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_13(self):
        try:
            bool_0 = True
            connection_0 = module_0.Connection(bool_0)
            bool_1 = False
            set_0 = {connection_0, bool_1, connection_0}
            var_0 = connection_0.__rpc__(set_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
