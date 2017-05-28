__AUTHOR__	= "Getsu"
__DATE__	= "28/05/2017"
__VERSION__	= "1.0"
__GITHUB__	= "https://github.com/alanjsil/MultiMail"
__LICENCA__ = "GNU General Public License v3.0"

import subprocess
import urllib3


def update_client_version(version):
    with open("versao.txt", "r") as vnum:
        if vnum.read() != version:
            return True
        else:
            return False


def main():
    version = urllib3.request.urlopen("https://raw.githubusercontent.com/alanjsil/MultiMail/master/versao.txt").read()
    if update_client_version(version) is True:
        subprocess.call(["git", "pull", "origin", "master"])
        return "[*] Updated to latest version: v{}..".format(version)
    else:
        return "[*] You are already up to date with git origin master."


if __name__ == '__main__':
    print("[*] Checking version information..")
    print(main())
