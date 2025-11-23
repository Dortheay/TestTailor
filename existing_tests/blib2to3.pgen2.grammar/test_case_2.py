import unittest
import timeout_decorator
import blib2to3.pgen2.grammar as module_0

class Test_Grammar_3(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_2(self):
        str_0 = 'M8Nw.&\x0b&}Hd<C-8f'
        grammar_0 = module_0.Grammar()
        grammar_0.dump(str_0)
        str_1 = 'Oh|=6~.pzOSYQ'
        grammar_0.load(str_0)
        grammar_1 = module_0.Grammar()
        grammar_0.dump(str_1)

if __name__ == "__main__":
    unittest.main()
