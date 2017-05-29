__AUTHOR__	= "Getsu"
__DATE__	= "28/05/2017"
__VERSION__	= "1.0"
__GITHUB__	= "https://github.com/alanjsil/MultiMail"
__LICENCA__ = "GNU General Public License v3.0"

import subprocess
import urllib.request

def update_client_version(version):
    with open("versao.txt", "rb") as vnum:
        if vnum.read() != version:
            return True
        else:
            return False

def main():
    version = urllib.request.urlopen("https://raw.githubusercontent.com/alanjsil/DistMail/master/versao.txt").read()
    if update_client_version(version) is True:
        subprocess.call(["git", "pull", "origin", "master"])
        return "[*] Atualize para a vesão mais recente: v%s."%version.decode("utf-8")
    else:
        return "[*] Voce esta com a versão mais atual."

if __name__ == '__main__':
    print("[*] Checando a versão...")
    print(main())