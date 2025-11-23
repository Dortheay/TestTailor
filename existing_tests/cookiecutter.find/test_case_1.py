import unittest
import timeout_decorator
import cookiecutter.find as module_0

class Test_Find_2(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        try:
            bytes_0 = b'{`\x9b=#t'
            var_0 = module_0.find_template(bytes_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
