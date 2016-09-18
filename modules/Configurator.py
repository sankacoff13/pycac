#
#   Configurator.py
#
#   Handles configuration options
################################################################################

import argparse

class Configurator():
    """Handles configuration options"""

    def __init__(self):
        """Initialize the class"""
        self.parser = argparse.ArgumentParser(description=
            """A Python interface to the Cloud at Cost API""")
        self.addOptions()

    def addOptions(self):
        """Add arguments to be parsed from the command-line"""
        self.parser.add_argument("-k", "--apiKey", dest="apikey", required=True,
                                 help="Cloud at Cost API Key")
        self.parser.add_argument("-l", "--login", dest="login", required=True,
                                 help="Cloud at Cost login")

    def getConfig(self):
        """Parse configuration options and return them as a dictionary"""
        return self.parser.parse_args().__dict__

