import unittest
import timeout_decorator
import ansible.module_utils.connection as module_0

class Test_Connection_3(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_2(self):
        try:
            bytes_0 = b'u\xc0%p\xa2}\xa7\xd5'
            connection_0 = module_0.Connection(bytes_0)
            set_0 = {connection_0}
            var_0 = module_0.send_data(connection_0, set_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
