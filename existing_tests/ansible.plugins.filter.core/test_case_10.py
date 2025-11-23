import unittest
import timeout_decorator
import ansible.plugins.filter.core as module_0

class Test_Core_11(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_10(self):
        try:
            str_0 = ' \'5pXSrw K"IA\x0bp'
            bytes_0 = b'\xcd\x1d\xe6\xcb\xbe4\xb7"B\xf5\xd2\xe7\xb2"'
            var_0 = module_0.to_uuid(str_0, bytes_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
