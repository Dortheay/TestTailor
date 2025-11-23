import unittest
import timeout_decorator
import cookiecutter.prompt as module_0

class Test_Prompt_5(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_4(self):
        try:
            str_0 = 'wB4JIqZ<vG'
            var_0 = module_0.process_json(str_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
