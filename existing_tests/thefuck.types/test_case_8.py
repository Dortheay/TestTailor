import unittest
import timeout_decorator
import thefuck.types as module_0

class Test_Types_9(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_3(self):
        str_0 = 'wAnh2\x0b\t'
        bytes_0 = b'\x07\x16\xf6\x1e\xd6\xd1\xf4\xaf\xe6\x9c\x95\xdf\xbf'
        command_0 = module_0.Command(str_0, bytes_0)
        var_0 = command_0.update()

if __name__ == "__main__":
    unittest.main()
