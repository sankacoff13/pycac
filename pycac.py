#
#   pycac.py
#
#   Python wrapper for the Cloud at Cost API.
###############################################################################

from modules import Configurator, Networking

class PyCac():

    def __init__(self):
        self.configurator = Configurator.Configurator()
        self.config = None
        self.net = None

    def main(self):
        self.config = self.configurator.getConfig()
        self.net = Networking.Networking(self.config["apikey"],
                                         self.config["login"])
        print self.net.post("renameserver.php", {"sid" : 12345,
                                                 "name" : "API Testing"})
        print self.net.get("listservers.php")

if __name__ == '__main__':
    pc = PyCac()
    pc.main()

