
try:
    import _winreg as winreg
except ImportError:
    import winreg
import os


def get_shared_cache_folder():
    """
    Look in the registry for the configured cache folder.
    If there is no entry, then we create one.
    :return:
    """
    winreg.aReg = winreg.ConnectRegistry(None, winreg.HKEY_CURRENT_USER)
    try:
        key = winreg.OpenKey(winreg.aReg, r"SOFTWARE\CCP\EVEONLINE")
        path, _ = winreg.QueryValueEx(key, "CACHEFOLDER")
    except OSError:
        return None
    return path


def set_shared_cache_folder(folder_path):
    if not os.path.isdir(folder_path):
        try:
            os.makedirs(folder_path)
        except OSError:
            raise ValueError("Could not create directory {}".format(folder_path))
    folder_path = os.path.normpath(folder_path) + os.sep

    key_eveonline = winreg.CreateKey(winreg.aReg, r"SOFTWARE\CCP\EVEONLINE")
    winreg.SetValueEx(key_eveonline, "CACHEFOLDER", 0, winreg.REG_SZ, folder_path)

    key_eveprobe = winreg.CreateKey(winreg.aReg, r"SOFTWARE\CCP\EVEPROBE")
    winreg.SetValueEx(key_eveprobe, "CACHEFOLDER", 0, winreg.REG_SZ, folder_path)


def get_index_path(hint):
    return hint
