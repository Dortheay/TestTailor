import unittest
import timeout_decorator
import typesystem.fields as module_0
import decimal as module_1

class Test_Fields_73(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_72(self):
        try:
            object_0 = module_0.Object()
            bytes_0 = None
            dict_0 = {}
            tuple_0 = ()
            str_0 = 'oQKw\tBJY%yH!}'
            list_0 = [dict_0, bytes_0, dict_0]
            number_0 = module_0.Number(exclusive_maximum=tuple_0, precision=str_0, multiple_of=list_0, **dict_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
