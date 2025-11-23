import unittest
import timeout_decorator
import ansible.cli.arguments.option_helpers as module_0

class Test_Option_helpers_16(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_15(self):
        try:
            bytes_0 = b'\x13\xcdB\xb2\xc5B\xefX\xd6\x8e\x17\xe5\x96\xbc$u\x14'
            var_0 = module_0.add_runas_prompt_options(bytes_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
