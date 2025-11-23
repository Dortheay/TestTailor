import unittest
import timeout_decorator
import ansible.cli.doc as module_0

class Test_Doc_2(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        float_0 = 1557.002
        str_0 = None
        var_0 = module_0.add_collection_plugins(float_0, str_0)

if __name__ == "__main__":
    unittest.main()
