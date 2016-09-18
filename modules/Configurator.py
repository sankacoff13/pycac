#
#   Configurator.py
#
#   Handles configuration options
################################################################################

import argparse
import json

class Configurator():
    """Handles configuration options"""

    def __init__(self):
        """Initialize the class"""
        self.parser = argparse.ArgumentParser(description=
            """A Python interface to the Cloud at Cost API""")
        self.addOptions()

    def addOptions(self):
        """Add arguments to be parsed from the command-line"""
        self.parser.add_argument("-k", "--apiKey", dest="apiKey",
                                 help="Cloud at Cost API Key (overrides cfg)")
        self.parser.add_argument("-l", "--login", dest="login",
                                 help="Cloud at Cost login (overrides cfg)")
        self.parser.add_argument("-f", "--cfgFile", dest="cfgFile",
                                 required=False,
                                 help="Configuration file (JSON)")

    def parseCfgFile(self, args, filename):
        """Reads options from a JSON formatted file"""
        with open(filename) as fd:
            fileArgs = json.load(fd)

            for farg in fileArgs:
                try:
                    if args[farg] is None:
                        args[farg] = fileArgs[farg]
                except KeyError:
                    print "Ignoring option: " + farg
                    continue
            fd.close()

        return args

    def validateConfig(self, args):
        """Validates the config options"""
        if args["apiKey"] is None:
            print "Error: missing apiKey"
            self.parser.print_help()
            exit()

        if args["login"] is None:
            print "Error: missing login"
            self.parser.print_help()
            exit()

    def getConfig(self):
        """Parse config options and return them as a dictionary"""
        args = self.parser.parse_args()

        if args.__dict__["cfgFile"]:
            args = self.parseCfgFile(args.__dict__, args.__dict__["cfgFile"])

        self.validateConfig(args)

        return args

