import unittest
import timeout_decorator
import ansible.parsing.splitter as module_0

class Test_Splitter_17(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_8(self):
        try:
            str_0 = '*Vw^OLF.o|{%a5A@TVoh'
            var_0 = module_0.split_args(str_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
