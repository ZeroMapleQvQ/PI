__author__ = 'jmh081701'
from win32api import RegOpenKeyEx, RegEnumKeyEx, RegQueryValueEx, RegCloseKey
import win32con


def get_all_installed_software():
    reg_root = win32con.HKEY_LOCAL_MACHINE
    reg_paths = [r"SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall",
                 r"SOFTWARE\Wow6432Node\Microsoft\Windows\CurrentVersion\Uninstall", r"Software\Microsoft\Windows\CurrentVersion\Uninstall"]
    rst_list = []
    for path in reg_paths:
        pkey = RegOpenKeyEx(reg_root, path)
        for item in RegEnumKeyEx(pkey):
            value_paths = path+"\\"+item[0]
            # print(value_paths)
            try:
                vkey = RegOpenKeyEx(reg_root, value_paths)
                DisplayName, key_type = RegQueryValueEx(
                    vkey, "DisplayName")
                UninstallString, key_type = RegQueryValueEx(
                    vkey, "UninstallString")
                # print({'name':DisplayName,'Uninstall string':UninstallString})
                rst_list.append((DisplayName, UninstallString))
                RegCloseKey(vkey)
            except:
                pass
        RegCloseKey(pkey)
    return rst_list


if __name__ == '__main__':
    software = get_all_installed_software()
    print(software)
