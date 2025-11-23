import unittest
import timeout_decorator
import ansible.module_utils.urls as module_0

class Test_Urls_31(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_30(self):
        try:
            bytes_0 = b'\x9c\xa6j\xf4>|\xac\xf0\x83\xb7I\x93&\x84\xc8\xcbr\x93F]'
            unix_h_t_t_p_connection_0 = module_0.UnixHTTPConnection(bytes_0)
            var_0 = unix_h_t_t_p_connection_0.connect()
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
