import unittest
import timeout_decorator
import ansible.vars.reserved as module_0

class Test_Reserved_4(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_3(self):
        bytes_0 = b'\xec1}t\xf0\xcb+\x071\xf1@_\xa2\x11'
        var_0 = module_0.warn_if_reserved(bytes_0)

if __name__ == "__main__":
    unittest.main()
