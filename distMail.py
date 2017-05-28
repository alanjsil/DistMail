__AUTHOR__	= "Getsu"
__DATE__	= "28/05/2017"
__VERSION__	= "1.0"
__GITHUB__	= "https://github.com/alanjsil/MultiMail"
__LICENCA__ = "GNU General Public License v3.0"

import banner
import emails
import os
import time
import updater

def limpa():
    os.system('cls' if os.name == 'nt' else 'clear')

def interromper():
    RED = '\33[91m'
    YELLOW = '\33[93m'

    limpa()
    banner.banners.banner2()
    print(RED+"[!]"+YELLOW+" VOCE CANCELOU!!!")
    exit()

def main():
    RED = '\33[91m'
    END = '\033[0m'

    try:
        banner.banners.banner1()
        # Escolhas no menu principal
        print("[1]GMAIL   [2]OUTLOOK   [3]CHECAR VERSÂO   [4]SAIR")
        try:

            escolha = int(input(">>> "))
            limpa()
            banner.banners.banner1()

            if escolha == 1:
                emails.gmail()
            elif escolha == 2:
                emails.outlook()
            elif escolha == 3:
                print(updater.main())
                time.sleep(2)
                limpa()
                main()
            elif escolha == 4:
                interromper()
            else:
                limpa()
                print(RED + '{--}ESCOLHA INCORRETA.{--}' + END)
                main()
        except ValueError:
            limpa()
            print(RED + '{--}ESCOLHA INCORRETA.{--}' + END)
            print(RED + '  {--}NÃO USE LETRAS.{--}' + END)
            main()

    except KeyboardInterrupt:
        interromper()

def aviso():
    try:
        YELLOW = '\33[93m'
        END = '\033[0m'
        banner.banners.inicial()
        NULL = input(YELLOW+"\nPressione ENTER para continuar."+END)
        limpa()
    except KeyboardInterrupt:
        interromper()

aviso()
main()
