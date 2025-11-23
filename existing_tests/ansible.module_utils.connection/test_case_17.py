import unittest
import timeout_decorator
import ansible.module_utils.connection as module_0

class Test_Connection_18(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_3(self):
        float_0 = -1254.42164
        connection_0 = module_0.Connection(float_0)

if __name__ == "__main__":
    unittest.main()
