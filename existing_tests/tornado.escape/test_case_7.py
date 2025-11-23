import unittest
import timeout_decorator
import tornado.escape as module_0

class Test_Escape_8(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_7(self):
        try:
            str_0 = 'zAp?\\mjQ~\x0bq'
            var_0 = module_0.url_unescape(str_0, str_0)
            bytes_0 = b'\x0e\x9b\xdd\xca'
            bytes_1 = b'B0\x12I\xac\xc1\xe0\x92\xafN\x80`\x8a.\xe0\xad'
            list_0 = [bytes_0, bytes_1]
            str_1 = 'Escapes a string so it is valid within HTML or XML.\n\n    Escapes the characters ``<``, ``>``, ``"``, ``\'``, and ``&``.\n    When used in attribute values the escaped strings must be enclosed\n    in quotes.\n\n    .. versionchanged:: 3.2\n\n       Added the single quote to the list of escaped characters.\n    '
            dict_0 = {str_0: list_0, str_1: list_0}
            any_0 = module_0.recursive_unicode(dict_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
