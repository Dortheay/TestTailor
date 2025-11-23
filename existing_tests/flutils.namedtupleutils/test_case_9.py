import unittest
import timeout_decorator
import types as module_0
import flutils.namedtupleutils as module_1
import collections as module_2

class Test_Namedtupleutils_10(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_9(self):
        int_0 = 173
        str_0 = 'setup_dir'
        list_0 = [int_0, str_0]
        var_0 = module_1.to_namedtuple(list_0)
        str_1 = "Return a string describing the file type if it exists.\n\n    This function processes the given ``path`` with\n    :obj:`~flutils.normalize_path`.\n\n    Args:\n        path (:obj:`str`, :obj:`bytes` or :obj:`Path <pathlib.Path>`):\n            The path to check for existence.\n\n    :rtype:\n        :obj:`str`\n\n        * ``''`` (empty string): if the given ``path`` does NOT exist; or,\n          is a broken symbolic link; or, other errors (such as permission\n          errors) are propagated.\n        * ``'directory'``: if the given ``path`` points to a directory or\n          is a symbolic link pointing to a directory.\n        * ``'file'``: if the given ``path`` points to a regular file or is a\n          symbolic link pointing to a regular file.\n        * ``'block device'``: if the given ``path`` points to a block device or\n          is a symbolic link pointing to a block device.\n        * ``'char device'``: if the given ``path`` points to a character device\n          or is a symbolic link pointing to a character device.\n        * ``'FIFO'``: if the given ``path`` points to a FIFO or is a symbolic\n          link pointing to a FIFO.\n        * ``'socket'``: if the given ``path`` points to a Unix socket or is a\n          symbolic link pointing to a Unix socket.\n\n    Example:\n        >>> from flutils.pathutils import exists_as\n        >>> exists_as('~/tmp')\n        'directory'\n    "
        list_1 = []
        ordered_dict_0 = module_2.OrderedDict()
        tuple_0 = (str_1, list_1, ordered_dict_0)
        var_1 = module_1.to_namedtuple(tuple_0)
        str_2 = 'NamedTuple'
        str_3 = None
        dict_0 = {str_2: int_0, str_3: str_3}
        bool_0 = True
        tuple_1 = (int_0, dict_0, int_0, bool_0)
        var_2 = module_1.to_namedtuple(tuple_1)
        str_4 = '<p(|9/WRKm)c!I:'
        var_3 = module_1.to_namedtuple(tuple_1)
        dict_1 = {str_4: str_4}
        var_4 = module_1.to_namedtuple(tuple_1)
        var_5 = module_1.to_namedtuple(tuple_1)
        str_5 = '/ZRa8#,t'
        str_6 = 'e-9[3R\rQ\\g&'
        str_7 = '__attr_map__ contains an invalid item of: '
        str_8 = 'url'
        dict_2 = {str_5: int_0, str_6: dict_1, str_7: dict_0, str_8: tuple_1}
        simple_namespace_0 = module_0.SimpleNamespace(**dict_2)
        var_6 = module_1.to_namedtuple(simple_namespace_0)

if __name__ == "__main__":
    unittest.main()
