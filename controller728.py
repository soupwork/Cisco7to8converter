#
#This is the Controller. 
#it handles the SSH connections out to the devices.
#it uses Netmiko.
#should this be one or more classes, or just functions

import netmiko

class RemoteRouter():
    """create a router object for Netmiko. """
    def __init__(self, ipaddy,loginID,testrouter):
        self.testrouter = testrouter
        self.ipaddy=ipaddy
        print("testrouter is ",self.testrouter)
        self.loginuser=loginID[0]
        self.loginpass=loginID[1]

  
    def testconnectToRouter(self,ipaddy):
        cisco = {
            'device_type': 'cisco_ios',
            'host': ipaddy,
            'username': self.loginuser,
            'password': self.loginpass,
            }

        net_connect = netmiko.ConnectHandler (**cisco)
        print(net_connect.find_prompt())
        hostname = net_connect.send_command('sh run | inc host')
        print("hostname is ", hostname)
        return(hostname)

    def connectToRouter(self):
        cisco = {
            'device_type': 'cisco_ios',
            'host': self.ipaddy,
            'username': self.loginuser,
            'password': self.loginpass,
            }

        net_connect = netmiko.ConnectHandler (**cisco)
        print(net_connect.find_prompt())
        output=net_connect.send_command('sh ip int brie')
        print(output)
        self.ShowVer(net_connect)
        hostname = self.showHost(net_connect)
        self.getUsernames(net_connect)
        usernames = self.getUsernames(net_connect)
        count=0
        for uname in usernames:
            print("username is ", uname)
            if "doug.sheehan" in uname:
                print("i'll delete this element")

            if "secret" in uname:
                print("discard username ", uname, " with secret assigned")
                del usernames[count]

            if "password 7" in uname:
                print("I'll convert this username/Password 7")

            if "password 0" in uname:
                print("I'll convert the plaintext password") 

            count+=1 

        print(usernames)  
        return(hostname,usernames)               


    def ShowVer(self,net_connect):
        getver=net_connect.send_command('sh version')
        print(getver)   

    def showHost(self,net_connect):
        net_connect.enable()
        print(net_connect.find_prompt())
        gethost=net_connect.send_command('sh run | inc host')
        print("gethost is ", gethost)

    def getUsernames(self, net_connect):
        net_connect.enable()
        unames=net_connect.send_command('sh run | inc username')
        #print("usernames are ", unames) 
        usernames=unames.splitlines()
        
        return(usernames)

if __name__ == "__main__":
    print ("controller is main")
    testloginID=('doug.sheehan','De34rfvc')
    print('username ', testloginID[0])
    testrouter=RemoteRouter('192.168.20.1', testloginID, '192.168.20.1')
    testrouter.testconnectToRouter()

