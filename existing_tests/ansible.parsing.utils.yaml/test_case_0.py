import unittest
import timeout_decorator
import ansible.parsing.utils.yaml as module_0

class Test_Yaml_1(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        try:
            list_0 = []
            var_0 = module_0.from_yaml(list_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
