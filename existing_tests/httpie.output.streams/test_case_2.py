import unittest
import timeout_decorator
import httpie.output.streams as module_0
import httpie.output.processing as module_1
import httpie.models as module_2

class Test_Streams_3(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_2(self):
        try:
            conversion_0 = module_1.Conversion()
            list_0 = []
            formatting_0 = module_1.Formatting(list_0)
            pretty_stream_0 = module_0.PrettyStream(conversion_0, formatting_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
