import unittest
import timeout_decorator
import ansible.module_utils.facts.network.linux as module_0

class Test_Linux_4(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_2(self):
        try:
            str_0 = '\n    Return the name of the current OS distribution, as a human-readable\n    string.\n\n    If *pretty* is false, the name is returned without version or codename.\n    (e.g. "CentOS Linux")\n\n    If *pretty* is true, the version and codename are appended.\n    (e.g. "CentOS Linux 7.1.1503 (Core)")\n\n    **Lookup hierarchy:**\n\n    The name is obtained from the following sources, in the specified order.\n    The first available and non-empty value is used:\n\n    * If *pretty* is false:\n\n      - the value of the "NAME" attribute of the os-release file,\n\n      - the value of the "Distributor ID" attribute returned by the lsb_release\n        command,\n\n      - the value of the "<name>" field of the distro release file.\n\n    * If *pretty* is true:\n\n      - the value of the "PRETTY_NAME" attribute of the os-release file,\n\n      - the value of the "Description" attribute returned by the lsb_release\n        command,\n\n      - the value of the "<name>" field of the distro release file, appended\n        with the value of the pretty version ("<version_id>" and "<codename>"\n        fields) of the distro release file, if available.\n    '
            float_0 = -2012.359
            int_0 = 814
            linux_network_0 = module_0.LinuxNetwork(int_0)
            var_0 = linux_network_0.get_interfaces_info(str_0, linux_network_0, float_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
