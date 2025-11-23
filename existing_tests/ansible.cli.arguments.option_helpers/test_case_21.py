import unittest
import timeout_decorator
import ansible.cli.arguments.option_helpers as module_0

class Test_Option_helpers_22(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_21(self):
        try:
            var_0 = module_0.unfrack_path()
            var_1 = module_0.version()
            bytes_0 = b'\x0f\xd2k'
            float_0 = None
            bool_0 = True
            tuple_0 = (bytes_0, float_0, bool_0)
            float_1 = 1000.0
            float_2 = 702.986652
            unrecognized_argument_0 = module_0.UnrecognizedArgument(bytes_0, float_1, float_2)
            var_2 = module_0.add_runas_prompt_options(tuple_0, unrecognized_argument_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
