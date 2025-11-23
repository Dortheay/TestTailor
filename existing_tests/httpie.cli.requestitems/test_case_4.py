import unittest
import timeout_decorator
import httpie.cli.argtypes as module_0
import httpie.cli.requestitems as module_1

class Test_Requestitems_5(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_4(self):
        try:
            str_0 = "\n    Parse `s` and update `defaults` with the parsed values.\n\n    >>> parse_format_options(\n    ... defaults={'json': {'indent': 4, 'sort_keys': True}},\n    ... s='json.indent:2,json.sort_keys:False',\n    ... )\n    {'json': {'indent': 2, 'sort_keys': False}}\n\n    "
            str_1 = ', */*;q=0.5'
            str_2 = 'store_true'
            key_value_arg_0 = module_0.KeyValueArg(str_1, str_1, str_0, str_2)
            str_3 = module_1.process_data_embed_file_contents_arg(key_value_arg_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
