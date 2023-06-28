import hashlib
import os

default_psw = 'b109f3bbbc244eb82441917ed06d618b9008dd09b3befd1b5e07394c706a8bb980b1d7785e5976ec049b46df5f1326af5a2ea6d103fd07c95385ffab0cacbc86'


# hash password and check with registered hash
def check_password(psw: str):
    hashGen = hashlib.sha512()
    hashGen.update(psw.encode('utf-8'))
    return os.environ.get("psw_hash", default_psw) == hashGen.hexdigest()
