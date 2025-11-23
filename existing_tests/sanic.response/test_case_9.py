import unittest
import timeout_decorator
import sanic.response as module_0

class Test_Response_10(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_2(self):
        str_0 = '[PKDG/$$ct{;,:$Cn['
        var_0 = module_0.stream(str_0, str_0)

if __name__ == "__main__":
    unittest.main()
