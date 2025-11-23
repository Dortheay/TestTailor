import unittest
import timeout_decorator
import ansible.module_utils.facts.compat as module_0

class Test_Compat_3(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_2(self):
        try:
            str_0 = "hJbd:l\x0cor{m#J,v'299u"
            var_0 = module_0.ansible_facts(str_0, str_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
