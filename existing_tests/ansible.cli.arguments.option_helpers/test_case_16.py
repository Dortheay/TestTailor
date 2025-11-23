import unittest
import timeout_decorator
import ansible.cli.arguments.option_helpers as module_0

class Test_Option_helpers_17(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_16(self):
        try:
            var_0 = module_0.unfrack_path()
            var_1 = module_0.version()
            bytes_0 = b'\x0f\xd2k'
            float_0 = None
            bool_0 = True
            tuple_0 = (bytes_0, float_0, bool_0)
            var_2 = module_0.add_meta_options(tuple_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
