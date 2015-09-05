import hashlib

__author__ = 'snorri.sturluson'

CHUNK_SZ = 8192

def calc_checksum(filename):
    """
    Calculates a checksum of the contents of the given file.
    :param filename:
    :return:
    """
    try:
        with open(filename, 'rb') as f:
            m = hashlib.md5()
            [m.update(chunk) for chunk in iter(lambda: f.read(CHUNK_SZ), b'')]
        return m.hexdigest()
    except IOError:
        return None