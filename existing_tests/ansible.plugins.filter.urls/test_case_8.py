import unittest
import timeout_decorator
import ansible.plugins.filter.urls as module_0

class Test_Urls_9(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_3(self):
        try:
            bytes_0 = b'\x90/\xe5\xa5&\\SY.'
            var_0 = module_0.do_urlencode(bytes_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
