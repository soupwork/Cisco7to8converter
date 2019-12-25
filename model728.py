#This is my Model. This is the Data.
#There will be three classes. 
# the will be a Log7to8, which keeps track of what the program is doing
# there will be a NetworkObject class, which is a Hostname, IP, 
#    and a list of Usernames with privledge level, password7, plaintext, secret8
#There will be a NetworkObjectGroup- do i need a class for this? it is really a list of
#   network Objects and file operations, maybe sorting.
#
import datetime

from convert7to8PKG.cisco7decrypt import decode

class NetworkObject():
    """Network object will have [index][hostname][ip address][log][verbose]
	[orig username][test username][password 7][plaintext][secret 8][notes and errors]
        """ 

    def __init__ (self,   hostname, ip, index=0, verbose=False,log=False,append=False, *args, **kwargs):
        """Network Object is the basic data object for this program. Hostname should be unique in a network.
            Hostname is manditory. IP is manditory. A hostname can have multiple IP's, but an IP can only 
            be assigned to one hostname. Log and verbose are optional. Login username and password for the 
            device (IP) are handled by the main program and never saved to a file. A network object might not 
            have any password 7's, in which case "No Password 7" will be in the notes field."""
            
        self.ip=ip
        print("IP Address is ",ip)
        print("Verbose messages is ", verbose)
        print("Log messages is ", log)
        print("Append messages to hostname-IP csv file is ", append)

    def checkUsername(self, username):
        pass
    
    def addUsername(self, username):
        pass

    def prepareUsernameCommand(self):
        pass





class NetworkObjectGroup():
    def __init__(self, filename, *args, **kwargs):
        if filename == "":
            #timestamp = datetime.datetime.now()
            datestamp = datetime.date.today()
            filename = "Convert7to8_" + str(datestamp)
        self.filename = filename
        print("filename is ",filename)
        with open(filename):
            pass

    

class Logmessages():
    """
        timestamp = datetime()
        timestamp = datetime.now()
        print ("timestamp is ", timestamp.now())
        """

if __name__ == "__main__":
    print("starting from model")
    #testfilename="testdata728.csv"
    #dataobject=convert_model(testfilename)
    #password7="111918160405041E007A7A"
    #plaintext=dataobject.decrypt(password7)
    #print("plaintext is ",plaintext)
    #testobj=NetworkObject(ip="192.168.20.1", verbose=True)
    testobj = NetworkObjectGroup(filename = "")