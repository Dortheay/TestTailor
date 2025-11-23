import unittest
import timeout_decorator
import ansible.modules.apt_repository as module_0

class Test_Apt_repository_4(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_3(self):
        try:
            invalid_source_0 = module_0.InvalidSource()
            var_0 = module_0.get_add_ppa_signing_key_callback(invalid_source_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
