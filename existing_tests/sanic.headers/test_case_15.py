import unittest
import timeout_decorator
import sanic.headers as module_0

class Test_Headers_16(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_5(self):
        str_0 = 'by'
        str_1 = '_obfuscatedAddress'
        str_2 = (str_0, str_1)
        str_3 = 'for'
        str_4 = '192.168.1.1'
        str_5 = (str_3, str_4)
        str_6 = 'host'
        str_7 = 'EXAMPLE.COM'
        str_8 = (str_6, str_7)
        str_9 = 'port'
        str_10 = '80'
        str_11 = (str_9, str_10)
        str_12 = 'proto'
        str_13 = 'HTTP'
        str_14 = (str_12, str_13)
        str_15 = 'path'
        str_16 = '/some%20path'
        str_17 = (str_15, str_16)
        str_18 = [str_2, str_5, str_8, str_11, str_14, str_17]
        str_19 = 'example.com'
        dict_0 = module_0.fwd_normalize(str_18)
        str_20 = 'unknown'
        str_21 = (str_3, str_20)
        str_22 = [str_21]
        dict_1 = module_0.fwd_normalize(str_22)
        str_23 = '2001:0db8:85a3:0000:0000:8a2e:0370:7334'
        str_24 = (str_3, str_23)
        str_25 = [str_24]
        dict_2 = module_0.fwd_normalize(str_25)
        str_26 = 'invalid_number'
        str_27 = (str_9, str_26)
        str_28 = [str_27]
        dict_3 = module_0.fwd_normalize(str_28)
        str_29 = (str_6, str_19)
        str_30 = (str_9, str_26)
        str_31 = 'HTTPS'
        str_32 = (str_12, str_31)
        str_33 = [str_29, str_30, str_32]
        dict_4 = module_0.fwd_normalize(str_33)

if __name__ == "__main__":
    unittest.main()
