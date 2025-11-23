import unittest
import timeout_decorator
import ansible.playbook.taggable as module_0

class Test_Taggable_1(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        try:
            taggable_0 = module_0.Taggable()
            list_0 = [taggable_0, taggable_0]
            bytes_0 = b'\xec\x06\xbe'
            str_0 = '=qqX/X<YE~s.$oDJu?E'
            str_1 = 'scheme'
            dict_0 = {str_0: list_0, str_1: taggable_0, str_1: list_0}
            var_0 = taggable_0.evaluate_tags(list_0, bytes_0, dict_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
