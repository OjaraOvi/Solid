import unittest

class UIPlatform ():
    def login(self):
        pass
    def logOut(self):
        pass
    def log(self):
        pass

class ConsoleUI (UIPlatform):
    def login(self):
        pass
    def logOut(self):
        pass
    def log(self):
        raise Exception ("Me fui a la B")

class SwiftUI(UIPlatform):
    def login(self):
        pass
    def logOut(self):
        pass
    def log(self):
        print("Yo funciono de forma correcta :)")

class UI():
    def __init__(self, platform):
        self.platform = platform
    def loginAndLog(self):
        self.platform.login()
        self.platform.log()

if __name__ == '__main__':
    # uiAux = ConsoleUI()
    # ui.log()
    uiAux = SwiftUI()
    ui = UI(uiAux)
    ui.loginAndLog()