class banners(object):

    def banner1():
        red = "\033[91m"
        print(red+ """
          ____      _
         / ___| ___| |_ ___ _   _
        | |  _ / _ \ __/ __| | | |
        | |_| |  __/ |_\__ \ |_| |
         \____|\___|\__|___/\__,_|
        """)

    def banner2():
        print("ALAN")

if __name__ == '__main__':
    a = banners.banner1()