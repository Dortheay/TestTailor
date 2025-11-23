import unittest
import timeout_decorator
import pymonet.maybe as module_0
import builtins as module_1

class Test_Maybe_4(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_3(self):
        try:
            bytes_0 = b'\xd5\x13\xf4~\xe4\xab\x8c\xe2\xe0\xffHu.\xfd'
            str_0 = '\n        Transform Box into Validation.\n\n        :returns: failed Validation monad with previous value as error\n        :rtype: Validation[None, [A]]\n        '
            bool_0 = False
            maybe_0 = module_0.Maybe(str_0, bool_0)
            var_0 = maybe_0.filter(bytes_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
