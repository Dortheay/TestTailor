import unittest
import timeout_decorator
import ansible.cli.arguments.option_helpers as module_0

class Test_Option_helpers_13(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_12(self):
        try:
            str_0 = 'Invalid role requirements file, it must end with a .yml or .yaml extension'
            var_0 = module_0.add_inventory_options(str_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
