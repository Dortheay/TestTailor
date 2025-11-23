import unittest
import timeout_decorator
import ansible.utils.listify as module_0

class Test_Listify_1(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        try:
            bytes_0 = b'\x02\xfcuh/?8\x97g'
            set_0 = {bytes_0}
            var_0 = module_0.listify_lookup_plugin_terms(bytes_0, set_0, bytes_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
