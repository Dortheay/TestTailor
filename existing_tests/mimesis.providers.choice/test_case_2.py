import unittest
import timeout_decorator
import mimesis.providers.choice as module_0

class Test_Choice_3(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        try:
            choice_0 = module_0.Choice()
            bytes_0 = b'P\x9b\xde{\x97d\x8a\x8c\xd5\xec\xcc\x18'
            int_0 = 1765
            var_0 = choice_0.__call__(bytes_0, int_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
