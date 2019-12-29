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
"""
#
#
#Sample input lines
#
# python main728.py -f test.csv -ip 192.168.0.1 -ip 192.168.1.1 -ip 192.168.20.1
# python main728.py -p7 111918160405041E007A7A
# python main728.py -p7 13351601181B0B382F747B
#
import argparse
import getpass
import datetime
import netmiko
#timestamp=datetime.datetime.now()
#import convert7to8PKG.cisco7decrypt2 as pw7de
from convert7to8PKG.cisco7decrypt import decode
import convert7to8PKG.model728 as model
import convert7to8PKG.view728CLI as viewCLI
import convert7to8PKG.controller728 as controller



class CLIparams():
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
        inputargs.add_argument('-verbose',action='store_true')

        inputargs.add_argument('-f', action='store_true',
            help='This option allowers user to specify a file for input or append.')
        
        inputargs.add_argument('-ip',action='append',
            help='use this option to specify one or more ip addresses to change')

        cliargs = inputargs.parse_args()
        self.filename = cliargs.f
        #testing
        self.filename = "testdata728.csv"
        if self.filename:
            checkFile = model.Filechecks(self.filename)
            checkFile.checkFilename()
            self.initialDict=checkFile.retDefaultDict()
            print("initial dictionary is ", self.initialDict)

        self.pass7 = cliargs.p7
        self.gui = cliargs.gui
        self.tr = cliargs.tr
        self.verbose = cliargs.verbose
        self.log = cliargs.log
        self.logfile = cliargs.logfile
        if self.logfile: #if a logfile is provided, logging must be desired
            self.log=True
        self.ip = cliargs.ip
        #self.
        print("cliargs is ", cliargs)
        print("Testrouter/SHArouter is ", self.tr)
        print(" verbose is ", self.verbose)
        print("filename is ", self.filename)
        print("CLI Password 7 is ", self.pass7)
        print("ip is ", self.ip)

    def setTestOptions(self):
        """this is manually setting options that ought to be passed in from the command line.
            It will probably be removed later.
            This is called from Main, after options have been set in CLIparams Init"""
        self.filename="test.csv"
        
        #self.gui = true
        #self.tr = cliargs.tr
        #self.verbose = true
        #self.log = true
        #self.logfile = cliargs.logfile
        #self.ip = "192.168.20.1"

    
    def setOptiontuple(self):
        
        optiontuple=(self.verbose,self.log,self.filename,self.ip)
        return(optiontuple)

    def checkPW7(self):
        print("checkPW7")
        if self.pass7:
           print("password7 is not blank")
           #decrypt=pw7de.decrypt7()
           #plaintext=decrypt.decode(self.pass7)
           getlogin=False

        else:
            self.getlogin=True
            print("password7 is blank")
            plaintext=""
            #if GUI option, launch the GUI
            #if CLI option, launch the CLI

        return(plaintext)


if __name__ == "__main__":
    print("starting from main")
    options=CLIparams()
    print("options ",options)
    print("manually setting options for testing")
    options.setTestOptions()

    checkpw=options.checkPW7()
    optionsTuple=options.setOptiontuple()
    if not options.pass7:
        uid=viewCLI.LoginDetails() #login details is part of "view"
        loginID=uid.getLoginID()
        print("login id is ", loginID)
        if not options.tr:
            options.tr = options.ip 

        testcontroller=controller.RemoteRouter(options.ip,loginID,options.tr)
        testcontroller.testconnectToRouter(options.tr)

    else:
        #print("plaintext is ",checkpw) #this only applies for -p7
        print("this would be decrypting")
