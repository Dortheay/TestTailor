import unittest
import timeout_decorator
import ansible.utils.version as module_0

class Test_Version_8(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_7(self):
        try:
            bytes_0 = b'\xb5\xde$97\xce\xaf\xb3\xc4Ka\x87\xc3'
            numeric_0 = module_0._Numeric(bytes_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
