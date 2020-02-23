#
#This is the Controller. 
#it handles the SSH connections out to the devices.
#it uses Netmiko.
#should this be one or more classes, or just functions

import netmiko

class RemoteRouter():
    """create a router object for Netmiko. """
    def __init__(self,loginID,testrouter):
        self.testrouter = testrouter
        self.ipaddy=testrouter
        print("testrouter is ",self.testrouter)
        self.loginuser=loginID[0]
        self.loginpass=loginID[1]
        testroutername = self.getHostname(testrouter)
        if testroutername == "":
            print("unable to connect to test router")
        else:    
            print("testrouter is ", testroutername)
        
  
   
        

    def connectToRouter(self, ipaddy):
#username Username06 privilege 15 password 7 107E080A16001D1908547C
#username Username07 privilege 15 secret 8 $8$F/w85a6wmpTYZk$ZQOonJGorZG9GMhX2eMUtChZmumf/wWRglqt8XFUUOk
#all usernames will start with "username ". slice off first 10 chars, then go to next space.
#"secret 8"(with the space) means I am not just flagging on the word secret in a username or other field
#
        self.namelist = []
        self.ipaddy = ipaddy
        cisco = {
            'device_type': 'cisco_ios',
            'host': self.ipaddy,
            'username': self.loginuser,
            'password': self.loginpass,
            }

        try:
            net_connect = netmiko.ConnectHandler (**cisco)
            print(net_connect.find_prompt())
        except:
            print("unable to connect to host")    
            return

        output=net_connect.send_command('sh ip int brie')
        print(output)
        self.ShowVer(net_connect)
        hostname = self.showHost(net_connect)
        self.hostname=hostname
        self.getUsernames(net_connect)
        usernames = self.getUsernames(net_connect)
        count=0
        for uname in usernames:
            uname = uname[9:]
            space = uname.index(' ')
            print("username is ", uname[:space])
            if "doug.sheehan" in uname:
                print("i'll delete this element")

            if "secret 8" in uname or "secret 5" in uname:
                print("discard username ", uname, " with secret assigned")
                del usernames[count]

            if "password 7" in uname:
                print("I'll convert this username/Password 7")
                index7 = uname.index("password 7") + 11
                element=[uname[:space],uname[index7:],'']
                print(element)
                self.namelist.append(element)

            if "password 0" in uname:
                print("I'll convert the plaintext password") 

            count+=1 

        print(self.namelist)  
        return               
    #end connectToRouter

    def ShowVer(self,net_connect):
        getver=net_connect.send_command('sh version')
        print(getver)   


    def getHostname(self,ipaddy):
        cisco = {
            'device_type': 'cisco_ios',
            'host': ipaddy,
            'username': self.loginuser,
            'password': self.loginpass,
            }

        try:
            net_connect = netmiko.ConnectHandler (**cisco)
            print(net_connect.find_prompt())
        except:
            print("unable to connect to host")    
            return("")

        privlevel=net_connect.send_command('show priv')
        print(privlevel)
        if privlevel=="Current privilege level is 15":
            hostname = net_connect.send_command('sh run | inc host')
            self.hostname = hostname[9:]
            print("hostname is ", self.hostname)
        else:
            print("insufficient Privilege Level")  
            self.hostname=''  
        return(self.hostname)

    def showHost(self,net_connect):
        net_connect.enable()
        print(net_connect.find_prompt())
        gethost=net_connect.send_command('sh run | inc host')
        self.hostname=gethost[9:]
        print("showhost is ", self.hostname)
        return(self.hostname)

    def getUsernames(self, net_connect):
        net_connect.enable()
        unames=net_connect.send_command('sh run | inc username')
        #print("usernames are ", unames) 
        usernames=unames.splitlines()
        
        return(usernames)

if __name__ == "__main__":
    print ("controller is main")
    testloginID=('doug.sheehan','doug.sheehan')
    print('username ', testloginID[0])
    testrouterIP="192.168.20.1"
    testrouter = RemoteRouter(testloginID, testrouterIP)
    hostname = testrouter.getHostname(testrouterIP)
    print('hostname of test router is', hostname)

