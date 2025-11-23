import unittest
import timeout_decorator
import ansible.module_utils.common.dict_transformations as module_0

class Test_Dict_transformations_4(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_3(self):
        try:
            bytes_0 = b'\xbd\xcf\x04\x87\xe8\xe5\x8e\xfal\x0b'
            str_0 = 'Jk=`bZ;;S\x0b&U\x0bPR<'
            dict_0 = {str_0: str_0, bytes_0: str_0}
            float_0 = 0.001
            var_0 = module_0.camel_dict_to_snake_dict(dict_0, float_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
