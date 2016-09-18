#
#   pycac.py
#
#   Python wrapper for the Cloud at Cost API.
###############################################################################

from modules import Configurator, Networking
import json

class PyCac():

    def __init__(self):
        """Initializes the class"""
        self.configurator = Configurator.Configurator()
        self.config = None
        self.net = None
        self.config = self.configurator.getConfig()
        self.net = Networking.Networking(self.config["apikey"],
                                         self.config["login"])

    def error(self, msg):
        """Handles errors in commands"""
        return msg

    # There is an issue right now with the API not getting an IP
    def build(self, cpu, ram, storage, os):
        """Build a server from available resources"""
        if 0 >= cpu or 16 < cpu:
            return self.error("Bad CPU value")

        if ram % 4 or ram < 0 or ram > 32768:
            return self.error("Bad RAM value")

        if storage < 0 or storage > 1000:
            return self.error("Bad storage value")

        templates = json.loads(self.listTemplates())["data"]
        for template in templates:
            if str(os) == template["ce_id"]:
                return self.net.post("cloudpro/build.php", {"cpu":cpu,
                                                            "ram":ram,
                                                            "storage":storage,
                                                            "os":os})

        return self.error("Bad OS specifier")


    # This completes successfully but no URL is returned
    def console(self, sid):
        """Request URL for console access"""
        return self.net.post("console.php", {"sid":sid})

    def delete(self, sid):
        """Delete a server to add resources"""
        return self.net.post("cloudpro/delete.php", {"sid":sid})

    def listServers(self):
        """Lists all servers on the account"""
        return self.net.get("listservers.php")

    # Currently there is a bug on their end with this API call
    def listTasks(self):
        """List all tasks in operation"""
        return self.net.get("listtasks.php")

    def listTemplates(self):
        """List all templates available"""
        return self.net.get("listtemplates.php")

    def powerOp(self, sid, action):
        """Activate server power operations"""
        onKeys = ["poweron", "on", "up"]
        offKeys = ["poweroff", "off", "down", "shutdown"]
        resKeys = ["reset", "reboot", "bounce"]
        action = action.lower()

        if action in onKeys:
            action = "poweron"
        elif action in offKeys:
            action = "poweroff"
        elif action in resKeys:
            action = "reset"
        else:
            return self.error("Bad power action")

        return self.net.post("powerop.php", {"sid":sid, "action":action})

    def rdns(self, sid, hostname):
        """Modify the reverse DNS and hostname of the VPS"""
        return self.net.post("rdns.php", {"sid":sid, "hostname":hostname})

    def renameServer(self, sid, name):
        """Rename the server label"""
        return self.net.post("renameserver.php", {"sid":sid, "name":name})

    def resources(self):
        """Display resources available and resources used in cloud-pro"""
        return self.net.get("cloudpro/resources.php")

    def runmode(self, sid, mode):
        """Set the run mode of the server to either normal or safe """
        if mode not in ["normal", "safe"]:
            return self.error("Invalid mode")

        return self.net.post("runmode.php", {"sid":sid, "mode":mode})

if __name__ == '__main__':
    pc = PyCac()
    print pc.listServers()

