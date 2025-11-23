import unittest
import timeout_decorator
import flutils.txtutils as module_0

class Test_Txtutils_8(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_7(self):
        try:
            int_0 = 20
            ansi_text_wrapper_0 = module_0.AnsiTextWrapper(int_0, max_lines=int_0)
            str_0 = "The given value for 'position', %r, must be an 'int' between (%r) and (%r)."
            str_1 = ansi_text_wrapper_0.fill(str_0)
            str_2 = ansi_text_wrapper_0.fill(str_0)
            str_3 = "A Finder that is used by Python's import to provide a\n    :obj:`ModuleSpec <importlib.machinery.ModuleSpec>` for a cherry-picking\n    module package.\n\n    This finder is a singleton, in that, on first use of\n    :obj:`~flutils.cherry_pick` this finder object is added to the top of\n    :obj:`sys.meta_path`.  Each subsequent use of :obj:`~flutils.cherry_pick`\n    will use the same object.\n\n    This object is used to cache a cherry-picking-module's data from a\n    module-package that is using the :obj:`~flutils.cherry_pick` function.\n\n    The :obj:`ModuleSpec <importlib.machinery.ModuleSpec>` created in this\n    finder's ``find_spec()`` method, will be set to use the custom\n    :obj:`~_CherryPicker <flutils.moduleutils._CherryPick>` loader.\n    Additionally, the cached data will be added to the spec's loader_state.\n    The loader_state (cached cherry-picking-module data) will be used by\n    :obj:`~_CherryPicker <flutils.moduleutils._CherryPick>` loader to create\n    the cherry-picked-module.\n    "
            str_4 = ansi_text_wrapper_0.fill(str_3)
            int_1 = -2713
            str_5 = ''
            str_6 = ansi_text_wrapper_0.fill(str_5)
            ansi_text_wrapper_1 = module_0.AnsiTextWrapper(int_0, int_1, max_lines=int_1, placeholder=str_0)
            str_7 = ansi_text_wrapper_1.fill(str_1)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
