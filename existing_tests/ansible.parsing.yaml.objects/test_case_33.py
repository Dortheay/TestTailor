import unittest
import timeout_decorator
import ansible.parsing.yaml.objects as module_0
import ansible.module_utils.common.text.converters as module_1

class Test_Objects_34(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_9(self):
        try:
            ansible_unicode_0 = module_0.AnsibleUnicode()
            tuple_0 = (ansible_unicode_0,)
            str_0 = '915;qQ2&Z:N%@O7k2y'
            str_1 = "\n- hosts: all\n  tasks:\n    - import_role:\n        name: myrole\n\n    - name: Run tasks/other.yaml instead of 'main'\n      import_role:\n        name: myrole\n        tasks_from: other\n\n    - name: Pass variables to role\n      import_role:\n        name: myrole\n      vars:\n        rolevar1: value from task\n\n    - name: Apply condition to each task in role\n      import_role:\n        name: myrole\n      when: not idontwanttorun\n"
            str_2 = 'g;!r~T4'
            dict_0 = {str_0: str_0, str_1: str_0, str_0: str_1, str_2: str_1}
            ansible_sequence_0 = module_0.AnsibleSequence(**dict_0)
            list_0 = [ansible_sequence_0, dict_0]
            ansible_vault_encrypted_unicode_0 = module_0.AnsibleVaultEncryptedUnicode(list_0)
            var_0 = ansible_vault_encrypted_unicode_0.__gt__(tuple_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
