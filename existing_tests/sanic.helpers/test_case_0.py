import unittest
import timeout_decorator
import sanic.helpers as module_0

class Test_Helpers_1(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        bytes_0 = b'7\xe3\xcab'
        var_0 = module_0.is_entity_header(bytes_0)

if __name__ == "__main__":
    unittest.main()
