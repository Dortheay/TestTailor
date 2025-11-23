import unittest
import timeout_decorator
import ansible.cli.console as module_0

class Test_Console_18(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_7(self):
        try:
            str_0 = '\n        Publishes a collection to a Galaxy server and returns the import task URI.\n\n        :param collection_path: The path to the collection tarball to publish.\n        :return: The import task URI that contains the import results.\n        '
            str_1 = '\n        Takes a string and tries to parse it as a variable definition. Returns\n        the key and value if successful, or raises an error.\n        '
            bytes_0 = b'\x06\xeaNA\xe0\xfd9i'
            console_c_l_i_0 = module_0.ConsoleCLI(bytes_0)
            float_0 = -3222.67
            console_c_l_i_1 = module_0.ConsoleCLI(float_0)
            var_0 = console_c_l_i_1.get_names()
            list_0 = [str_0]
            console_c_l_i_2 = module_0.ConsoleCLI(list_0)
            var_1 = console_c_l_i_2.do_check(console_c_l_i_1)
            console_c_l_i_3 = module_0.ConsoleCLI(str_1)
            var_2 = console_c_l_i_3.do_become(str_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
