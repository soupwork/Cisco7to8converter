#Dougs Cisco Password 7 to Secret 8 Converter
# copyright 2019 Douglas J. Sheehan
# This is my Main Program

""" 
This program will convert a cisco password 7 (insecure) into a cisco secret 8 (sha256)
This program will input a csv (data: hostname, IP Address, Username, password7)
This program will SSH to a router, and use that to generate the SHA256 secret8
The csv will have a space res'd for the secret 8
The program will add to the csv, the plaintext password and secret8. This will be turned off in production.
The program can also be used to only input a password 7 and display a plaintext word.

testmain728.py is for testing the model and bypassing the joys of needing to pass in parameters through 
the command line.

"""
#
#filename should just be a csv list of target ip addresses
#Sample input lines
#
# python main728.py -f "e:\dougsprogs\Convert728\convert7to8PKG\\testdata728.csv"
# python main728.py -f test.csv -ip 192.168.0.1 -ip 192.168.1.1 -ip 192.168.20.1
# python main728.py -f test.csv -ip 192.168.0.1 -tr 192.168.20.1
# python main728.py -help
# python main728.py -p7 13351601181B0B382F747B
#
import argparse
import getpass
import datetime
import netmiko
#timestamp=datetime.datetime.now()

from convert7to8PKG.cisco7decrypt import decode
import convert7to8PKG.model728 as model
import convert7to8PKG.view728CLI as viewCLI
import convert7to8PKG.controller728 as controller



class CLIparams:
    def __init__(self):
        inputargs = argparse.ArgumentParser()
        inputargs.add_argument('-p7',
            help='put in a password 7  after -p7 to have program decrypt and exit')
        inputargs.add_argument('-gui',action='store_true',
            help='this flag will launch the GUI, if I have finished it') 
        inputargs.add_argument('-tr',
            help='this is a testrouter or sharouter to generate/verify the sha256 secret works')     
        inputargs.add_argument('-log', action='store_true', 
            help='this will create a log file "Convert7to8_Log_datetime"')
        inputargs.add_argument('-logfile', help='same as log, but allows user to set filename')    
        inputargs.add_argument('-verbose',action='store_true',
            help='this will store extra detail in log and plaintext passwords \
                in datafile as well as hashes')

        inputargs.add_argument('-f', action='store',
            help='This option allowers user to specify a file for input or append.')

        inputargs.add_argument('-change', action='store_true', 
            help='when true(default), this flag will attempt to apply the change to router "')
        inputargs.add_argument('-verify', action='store_true', 
            help='when true(default), this flag will attempt to ssh into the router to verify \
                the changed password. It probably won\'t work with Tacacs or Radius')
        
        inputargs.add_argument('-ip',action='append',
            help='use this option to specify one or more ip addresses to change')

        cliargs = inputargs.parse_args()
        self.filename = cliargs.f
        #testing
        #self.filename = "testdata728.csv"
       
        self.pass7 = cliargs.p7
        self.cliDict={'IPADDRESS':cliargs.ip, 'TESTROUTER':cliargs.tr, 'LOG':cliargs.log , \
             'LOGFILE':cliargs.logfile ,'VERBOSE': cliargs.verbose, 'CHANGE':cliargs.change,'VERIFIY':cliargs.verify, 'FILENAME':cliargs.f ,'GUI':cliargs.gui}

       
    def setTestOptions(self):
        """this is manually setting options that ought to be passed in from the command line.
            It will probably be removed later.
            This is called from Main, after options have been set in CLIparams Init"""
        #self.filename="test.csv"
        #self.pass7 = '122D0E023C2C1A303D'
        #self.cliDict['IPADDRESS']=['192.168.20.1','192.168.20.1']
        #self.cliDict['TESTROUTER']= '192.168.20.1'

    def evalIPListAndFilenameTR(self,model):
        """this fn is to do a quick check on ip list and filename parms, and set TR if needed
            the order of evaluation is what I expect most, down to what I expect least"""
        self.fileOrIPorTR = True

        #no filename, no ip address,
        if not self.cliDict['FILENAME'] and not self.cliDict['IPADDRESS']:
            if self.cliDict['TESTROUTER']:
                self.cliDict['IPADDRESS'] = self.cliDict['TESTROUTER']
            else: # No filename,no ip address, no test router
                self.fileOrIPorTR=False

        elif self.cliDict['FILENAME'] and not self.cliDict['IPADDRESS']:
            """load up to 500 ip addresses from filename"""
            linecount = model.loadMaxIPlist(self.cliDict['FILENAME'])
            self.cliDict['IPADDRESS'] = model.objdict['IPADDRESS']

        print("self.cliDict['IPADDRESS'] should have a value by now,unless all three were blank.")
        print(self.cliDict['IPADDRESS'])

        if not self.cliDict['TESTROUTER'] and self.cliDict['IPADDRESS']:  #no TestRotuter Defined
            self.cliDict['TESTROUTER'] = '0.0.0.0'
            self.cliDict['TESTROUTER'] =  self.cliDict['IPADDRESS'][0]
            print(self.cliDict['TESTROUTER'])
            
        
        print("testrouter is ", self.cliDict['TESTROUTER'])    
        #else: #testrouter is provided
           # pass
        return(self.fileOrIPorTR)

    def showPW7(self):
        print("show PW7")
        plaintext = decode(self.pass7)
        getlogin=False
        print("pass 7 is ", self.pass7)
        print("plaintext is ", plaintext)
        return(plaintext)

def main():
    print("inside main fn")
    options=CLIparams()
    #*************************
    #options.setTestOptions()
    #*************************

    for key in options.cliDict:
        print("key ", key, "  ",options.cliDict[key])
    #print("manually setting options for testing")
    #options.setTestOptions()
    
   

    if options.pass7:
        print("Program is decrypting")
        plaintext=options.showPW7()

    else:   #password7 option does not have a value 
        mainmodel = model.InitializeModel(options.cliDict)   
        
        view = viewCLI.UserPrompts() 
        options.evalIPListAndFilenameTR(mainmodel)
        if not options.fileOrIPorTR:
            choice = view.noFileNoList()
            
            if choice[0] == "ip":
               options.cliDict['IPADDRESS'] = choice[1]
            if choice[0] == "filename":
                options.cliDict['FILENAME'] = choice[1]
            options.evalIPListAndFilenameTR(mainmodel)

        #loginID=view.getLoginID()
        # router = controller.RemoteRouter(loginID, options.cliDict['TESTROUTER'])

        # netobjgroup = model.NetworkObjectGroup(mainmodel.objdict)

        # router.ipaddy = '192.168.20.1'
        # router.connectToRouter()
        # newlist = router.namelist
        # for element in newlist:
        #     if element[1]:
        #         element[2]=decode(element[1])
        #     print(element, "\n")

       


if __name__ == "__main__":
    print("startiing from __main__")
    main()  


     #   testcontroller=controller.RemoteRouter(loginID,options.tr)
     #   hostname = testcontroller.getHostname(options.tr)
  
        #print("plaintext is ",checkpw) #this only applies for -p7


        #end main program
