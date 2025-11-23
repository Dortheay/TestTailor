import unittest
import timeout_decorator
import ansible.module_utils.connection as module_0

class Test_Connection_19(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_4(self):
        str_0 = 'diypT'
        int_0 = 29
        connection_0 = module_0.Connection(int_0)
        var_0 = connection_0.__getattr__(str_0)

if __name__ == "__main__":
    unittest.main()
