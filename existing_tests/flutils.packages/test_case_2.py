import unittest
import timeout_decorator
import flutils.packages as module_0

class Test_Packages_3(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_2(self):
        try:
            str_0 = "Convert a string with words separated by underscores to a camel-cased\n    string.\n\n    Args:\n        text (:obj:`str`): The camel-cased string to convert.\n        lower_first (:obj:`bool`, optional): Lowercase the first character.\n            Defaults to :obj:`True`.\n\n    :rtype: :obj:`str`\n\n    Examples:\n        >>> from flutils.strutils import underscore_to_camel\n        >>> underscore_to_camel('foo_bar')\n        'fooBar'\n        >>> underscore_to_camel('_one__two___',lower_first=False)\n        'OneTwo'\n    "
            str_1 = module_0.bump_version(str_0, str_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
