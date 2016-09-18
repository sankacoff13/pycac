#
#   Networking.py
#
#   Handles networking functionality.
################################################################################

import requests

class Networking():
    """Handles networking functionality"""

    def __init__(self, key, login):
        """Initialize the class"""
        self.key = key
        self.login = login
        self.baseUrl = "https://panel.cloudatcost.com/api/v1/"
        self.conn = self.configureNet()

    def configureNet(self):
        """Creates, configures and returns a connection object"""
        requests.packages.urllib3.disable_warnings()
        conn = requests.Session()
        conn.verify = False
        return conn

    def parseResponse(self, response):
        if response.status_code == 200:
            return response.text
        return str(response.status_code) + " - " + response.text

    def get(self, page):
        """Performs a get request of the specified page"""
        response = self.conn.get(self.baseUrl + page,
                                 params={'key':self.key, 'login':self.login})
        return self.parseResponse(response)

    def post(self, page, params):
        """Performs a post to the specified page with the given parameters"""
        data = params
        data["key"] = self.key
        data["login"] = self.login
        response = self.conn.post(self.baseUrl + page, data=data)
        return self.parseResponse(response)

