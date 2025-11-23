import unittest
import timeout_decorator
import ansible.module_utils.urls as module_0

class Test_Urls_17(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_16(self):
        try:
            tuple_0 = ()
            var_0 = module_0.get_channel_binding_cert_hash(tuple_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
