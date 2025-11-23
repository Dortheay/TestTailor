import unittest
import timeout_decorator
import ansible.template.safe_eval as module_0

class Test_Safe_eval_8(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_6(self):
        bytes_0 = b'q\xb6\xf7!\xb0P~\x9e\xd7<7Z\x14\xe8W\x12\xdcR'
        list_0 = []
        var_0 = module_0.safe_eval(bytes_0, list_0)

if __name__ == "__main__":
    unittest.main()
