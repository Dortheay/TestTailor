import unittest
import timeout_decorator
import youtube_dl.postprocessor.xattrpp as module_0

class Test_Xattrpp_2(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        x_attr_metadata_p_p_0 = module_0.XAttrMetadataPP()

if __name__ == "__main__":
    unittest.main()
