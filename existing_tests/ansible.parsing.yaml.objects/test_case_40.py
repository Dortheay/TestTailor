import unittest
import timeout_decorator
import ansible.parsing.yaml.objects as module_0
import ansible.module_utils.common.text.converters as module_1

class Test_Objects_41(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_16(self):
        try:
            str_0 = "\n        Action plugin handler for yum3 vs yum4(dnf) operations.\n\n        Enables the yum module to use yum3 and/or yum4. Yum4 is a yum\n        command-line compatibility layer on top of dnf. Since the Ansible\n        modules for yum(aka yum3) and dnf(aka yum4) call each of yum3 and yum4's\n        python APIs natively on the backend, we need to handle this here and\n        pass off to the correct Ansible module to execute on the remote system.\n        "
            str_1 = 'JlB'
            str_2 = None
            str_3 = 'yzdX%!=*]gx'
            dict_0 = {str_1: str_0, str_2: str_0, str_3: str_3, str_3: str_0}
            bool_0 = False
            ansible_vault_encrypted_unicode_0 = module_0.AnsibleVaultEncryptedUnicode(bool_0)
            var_0 = ansible_vault_encrypted_unicode_0.endswith(dict_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
