class banners(object):

    def color():
        BLUE = '\33[94m'
        RED = '\33[91m'
        WHITE = '\33[97m'
        YELLOW = '\33[93m'
        MAGENTA = '\033[1;35m'
        GREEN = '\033[1;32m'
        END = '\033[0m'

    def banner1():
        BLUE = '\33[94m'
        RED = '\33[91m'
        END = '\033[0m'

        print("""
         ________________________________________________
        |\         """+RED+"""  / ___| ___| |_ ___ _   _ """+END+"""          /|
        | \        """+RED+""" | |  _ / _ \ __/ __| | | |"""+END+"""         / |
        |  \       """+RED+""" | |_| |  __/ |_\__ \ |_| |"""+END+"""        /  |
        |   \      """+RED+"""  \____|\___|\__|___/\__,_|"""+END+"""       /   |
        |    \______________________________________/    |
        |                 """+BLUE+""" ____  __  __"""+END+"""                  |
        |                 """+BLUE+"""|  _ \|  \/  |"""+END+"""                 |
        |                 """+BLUE+"""| | | | |\/| |"""+END+"""                 |
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
        [+]Escolha arquivos de texto plano.

    """)

    def banner2():
        BLUE = '\33[94m'
        RED = '\33[91m'
        PRETO = '\033[97m'

        print("""
                 ________________________________________________
                |\         """ + RED + """  / ___| ___| |_ ___ _   _ """ + PRETO + """          /|
                | \        """ + RED + """ | |  _ / _ \ __/ __| | | |""" + PRETO + """         / |
                |  \       """ + RED + """ | |_| |  __/ |_\__ \ |_| |""" + PRETO + """        /  |
                |   \      """ + RED + """  \____|\___|\__|___/\__,_|""" + PRETO + """       /   |
                |    \______________________________________/    |
                |                 """ + BLUE + """  ____  __  __""" + PRETO + """                 |
                |                 """ + BLUE + """|  _ \|  \/  |""" + PRETO + """                 |
                |                 """ + BLUE + """| | | | |\/| |""" + PRETO + """                 |
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

if __name__ == '__main__':
    a = banners.banner1()
    b = banners.principal("A", "B", "C")
