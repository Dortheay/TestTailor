import unittest
import timeout_decorator
import collections as module_0
import flutils.codecs.raw_utf8_escape as module_1
import codecs as module_2

class Test_Raw_utf8_escape_12(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_7(self):
        try:
            str_0 = 'A loader that creates a module which defers loading until attribute\n    access.\n\n    This class is a "derivative work" of the Python\n    :obj:`importlib.util.LazyLoader`, and is:\n\n    `Copyright © 2001-2018 Python Software Foundation; All Rights Reserved\n    <https://bit.ly/2JzG17l>.`_\n\n    This class differs from :obj:`importlib.util.LazyLoader` in that it\n    uses the :obj:`~flutils.moduleutils._LazyModule` class and the\n    ``factory`` class method was removed.\n    '
            str_1 = '\x0c$'
            tuple_0 = module_1.encode(str_0)
            int_0 = 77
            tuple_1 = (str_0, int_0)
            tuple_2 = module_1.decode(tuple_1, str_1)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
