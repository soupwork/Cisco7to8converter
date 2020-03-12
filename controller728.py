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
        self.loginuser=loginID[0]
        self.loginpass=loginID[1]

        self.testcisco = {
            'device_type': 'cisco_ios',
            'host': self.testrouter,
            'username': self.loginuser,
            'password': self.loginpass,
            }
        # self.testcisco = {
        #     'device_type': 'cisco_ios',
        #     'host': '192.168.20.1',
        #     'username': self.loginuser,
        #     'password': self.loginpass,
        #     }
        net_connect = self.connectTestRouter(self.testrouter)
        if net_connect == "no connect":
            print("no connection")
            testroutername = ""
        else:    
            testroutername = self.getHostname(net_connect)
        
        if testroutername == "":
            print("unable to connect to test router")
        else:    
            print("remoterouter-testrouter is ", testroutername)
        
       
        

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
            if "doug.sheehan" in uname and len(usernames) > 1:
                response = net_connect.send_config_set('no username doug.sheehan')
                if '[confirm]' in response:
                    confirm = net_connect.send_command('y')
                   
            if "secret 8" in uname or "secret 5" in uname:
                print("ignore username ", uname, " with secret assigned")
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

    def connectTestRouter(self,netObjDict="", newuserstring=''):
        """the two funcitons of the testrouter is to verify that networking and
            netmiko are working right; secondly to generate the secret 8 hash. 

            """
    
        

        testcisco = {
            'device_type': 'cisco_ios',
            'host': self.testrouter,
            'username': self.loginuser,
            'password': self.loginpass,
            }

        print("now try to connect to testrouter")
        #print(testcisco)
        try:
            net_connect = netmiko.ConnectHandler (**testcisco)
            print(net_connect.find_prompt())
            
        except:
            print("unable to connect to host")    
            return("no connect")
        if not newuserstring:
            output=net_connect.send_command('sh ip int brie')
            print(output)
            self.ShowVer(net_connect)
            hostname = self.showHost(net_connect)
        else:
            print("in controller -testrouter new user string is ")
            print(newuserstring , "\n") 
            self.newtestuser(net_connect, netObjDict, testnewuserstring)   

        return (net_connect)              
    #end connectTestRouter

    def newtestuser(self, net_connect, netObjDict,testuserstring):
        testuser = netObjDict['TESTUSERNAME']
        print("test username is ", testuser)
        net_connect.send_config_set(testuserstring)
        unames = net_connect.send_command('sh run | inc test')
        unames = unames.splitlines()
        print("usernames from newtestuser are ", unames) 



    def ShowVer(self,net_connect):
        getver=net_connect.send_command('sh version')
        print(getver)   

    def getHostname(self,net_connect):
        #
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
        ipaddy = self.ipaddy
        self.ipaddy = self.testrouter
        net_connect.enable()
        unames = net_connect.send_command('sh run | inc username')
        #print("usernames are ", unames) 
        usernames=unames.splitlines()
        self.ipaddy = ipaddy
        return(usernames)

  


if __name__ == "__main__":
    print ("controller is main")
    loginuser = 'djs'
    loginpass = 'doug.sheehan'
    testloginID=(loginuser,loginpass)
    testrouterIP="192.168.20.1"

    testrouterobj = RemoteRouter(testloginID, testrouterIP)
    testNetworkObjDict = {'HOSTNAME':'testhostname','IPADDRESS':'192.168.20.1',
        'LOG':'n','VERBOSE':'n','ORIGUSERNAME':'Username01','TESTUSERNAME':'test', 
        'PASSWORD7':'053B071C325B411B1D5546','PLAINTEXT':'password','SECRET8':'',
        'CHANGE':'y','VERIFIED':'','NOTES-AND-ERRORS':''
        }

    testnewuserstring = "username test priv 15 alg sha secret password"
    testrouterobj.connectTestRouter(testNetworkObjDict, testnewuserstring)
    # hostname = testrouter.getHostname(testrouterIP)
    # print('hostname of test router is', hostname)

    # testcisco = {
    #         'device_type': 'cisco_ios',
    #         'host': testrouterIP,
    #         'username': loginuser,
    #         'password': loginpass,
    #         }

    # try:
    #     net_connect = netmiko.ConnectHandler (** testcisco)
    #     print(net_connect.find_prompt())
    # except:
    #     print("unable to connect to host")    
    

    # output=net_connect.send_command('sh ip int brie')
    # print(output)
