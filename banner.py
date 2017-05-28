__AUTHOR__	= "Getsu"
__DATE__	= "28/05/2017"
__VERSION__	= "1.0"
__GITHUB__	= "https://github.com/alanjsil/MultiMail"
__LICENCA__ = "GNU General Public License v3.0"

class banners(object):
    
    def banner1():
        BLUE = '\33[94m'
        RED = '\33[91m'
        END = '\033[0m'
        GREEN = '\033[1;32m'

        print("""
         ________________________________________________
        |\         """+RED+"""  / ___| ___| |_ ___ _   _ """+END+"""          /|        DistMail
        | \        """+RED+""" | |  _ / _ \ __/ __| | | |"""+END+"""         / |        Ferramenta para envio de
        |  \       """+RED+""" | |_| |  __/ |_\__ \ |_| |"""+END+"""        /  |        multiplos e-mails
        |   \      """+RED+"""  \____|\___|\__|___/\__,_|"""+END+"""       /   |
        |    \______________________________________/    |
        |                 """+BLUE+""" ____  __  __"""+END+"""                  |
        |  De: """+GREEN+"""DistMail   """+BLUE+"""|  _ \|  \/  |"""+END+"""                 |
        |  Para: """+GREEN+"""Alvo     """+BLUE+"""| | | | |\/| |"""+END+"""                 |
        |                 """+BLUE+"""| |_| | |  | |"""+END+"""                 |
        |                 """+BLUE+"""|____/|_|  |_|"""+END+"""                 |
        |________________________________________________|
        """)

        print("""
        [+] Trabalha com GMAIL e OUTLOOK
            [!] Seus dados estão seguros.
            [!] Ative a opção "Aplicativos menos seguro" para prosseguir.
                                """+RED+"""(Apenas no gmail)"""+END+"""
                    >> https://myaccount.google.com/lesssecureapps <<

        """)

    def banner2():
        BLUE = '\33[94m'
        RED = '\33[91m'
        PRETO = '\033[97m'
        GREEN = '\033[1;32m'
        END = '\033[0m'

        print("""
                 ________________________________________________
                |\         """ + RED + """  / ___| ___| |_ ___ _   _ """ + PRETO + """          /|
                | \        """ + RED + """ | |  _ / _ \ __/ __| | | |""" + PRETO + """         / |
                |  \       """ + RED + """ | |_| |  __/ |_\__ \ |_| |""" + PRETO + """        /  |
                |   \      """ + RED + """  \____|\___|\__|___/\__,_|""" + PRETO + """       /   |
                |    \______________________________________/    |
                |                 """ + BLUE + """ ____  __  __""" + PRETO + """                  |
                |  De: """+GREEN+"""DistMail   """+BLUE+"""|  _ \|  \/  |"""+END+"""                 |
                |  Para: """+GREEN+"""Alvo     """+BLUE+"""| | | | |\/| |"""+END+"""                 |
                |                 """ + BLUE + """| |_| | |  | |""" + PRETO + """                 |
                |                 """ + BLUE + """|____/|_|  |_|""" + PRETO + """                 |
                |________________________________________________|
                """)

    def conteudo(email, para, msg):
        print("""

                    [!]Seu E-mail : %s

                    [!]E-mail Alvo : %s

                    [!]Mensagem : %s

                    [!]Envio de Texto
                """ % (email, para, msg))

    def inicial():
        BLUE = '\33[94m'
        RED = '\33[91m'
        PRETO = '\033[97m'
        GREEN = '\033[1;32m'
        YELLOW = '\33[93m'
        WHITE = '\33[97m'
        END = '\033[0m'

        print("""
         ________________________________________________
        |\         """ + RED + """  / ___| ___| |_ ___ _   _ """ + PRETO + """          /|
        | \        """ + RED + """ | |  _ / _ \ __/ __| | | |""" + PRETO + """         / |
        |  \       """ + RED + """ | |_| |  __/ |_\__ \ |_| |""" + PRETO + """        /  |
        |   \      """ + RED + """  \____|\___|\__|___/\__,_|""" + PRETO + """       /   |
        |    \______________________________________/    |
        |                 """ + BLUE + """ ____  __  __""" + PRETO + """                  |
        |  De: """+GREEN+"""DistMail   """+BLUE+"""|  _ \|  \/  |"""+END+"""                 |
        |  Para: """+GREEN+"""Alvo     """+BLUE+"""| | | | |\/| |"""+END+"""                 |
        |                 """ + BLUE + """| |_| | |  | |""" + PRETO + """                 |
        |                 """ + BLUE + """|____/|_|  |_|""" + PRETO + """                 |
        |________________________________________________|
                        """)
        print("""\n
        """ + RED + """       [ Alerta de isenção de responsabilidade ]""" + YELLOW +  """
        """ + WHITE + """         Não sou responsável pelo uso indevido """ + YELLOW + """
        """ + WHITE + """                       ou fins ilegais.""" + YELLOW + """
        """ + WHITE + """               Use para """ + RED + """ TRABALHO"""+ WHITE + """ ou """ + RED + """ESTUDO""" + WHITE + """ !""")

if __name__ == '__main__':
    banners.inicial()
