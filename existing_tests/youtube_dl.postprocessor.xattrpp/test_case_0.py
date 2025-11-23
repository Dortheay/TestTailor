import unittest
import timeout_decorator
import youtube_dl.postprocessor.xattrpp as module_0

class Test_Xattrpp_1(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        try:
            float_0 = 909.8009
            x_attr_metadata_p_p_0 = module_0.XAttrMetadataPP()
            var_0 = x_attr_metadata_p_p_0.run(float_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
