import unittest
import timeout_decorator
import ansible.module_utils.connection as module_0

class Test_Connection_17(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_2(self):
        bytes_0 = b'\xa4\xa3\xcaXR\xf4\xf9\x88\x9a2z\x8f=\x7f'
        list_0 = [bytes_0]
        connection_error_0 = module_0.ConnectionError(list_0)

if __name__ == "__main__":
    unittest.main()
