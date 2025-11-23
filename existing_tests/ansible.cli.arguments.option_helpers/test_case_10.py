import unittest
import timeout_decorator
import ansible.cli.arguments.option_helpers as module_0

class Test_Option_helpers_11(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_10(self):
        try:
            bytes_0 = b'\xc5\xb4\xdd\xc0\xcf\x7f\xd7\x89V'
            var_0 = module_0.add_connect_options(bytes_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
