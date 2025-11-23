import unittest
import timeout_decorator
import ansible.module_utils.connection as module_0

class Test_Connection_4(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_3(self):
        try:
            list_0 = None
            var_0 = module_0.recv_data(list_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
