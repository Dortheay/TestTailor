import unittest
import timeout_decorator
import thefuck.rules.django_south_merge as module_0

class Test_Django_south_merge_1(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        try:
            bytes_0 = b'\xc9\xf6\xba\xd6E\x9bY\xce_9\xd0#\xf8\xb6\x9e\xbd\xcb\xf42'
            var_0 = module_0.match(bytes_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
