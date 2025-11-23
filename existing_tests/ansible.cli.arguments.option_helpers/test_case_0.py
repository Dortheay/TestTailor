import unittest
import timeout_decorator
import ansible.cli.arguments.option_helpers as module_0

class Test_Option_helpers_1(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        try:
            str_0 = 'Ab?US+fS,Tu]8@|+|'
            var_0 = module_0.add_runtask_options(str_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
