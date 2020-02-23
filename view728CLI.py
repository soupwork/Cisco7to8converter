#
#This is the CLI view. no GUI elements.
import getpass
import datetime
import os.path


class UserPrompts:
    def __init__(self):
        # self.username = input("enter the username to authenticate to router/switch: ")
        # self.pword=getpass.getpass("please enter password <hidden> :")
        # print ("username is :", self.username)
        print("init UserPrompts")

    def getLoginID(self):
        self.username = input("enter the username to authenticate to router/switch: ")
        self.pword=getpass.getpass("please enter password <hidden> :")
        print ("username is :", self.username)

        return(self.username,self.pword)
    
    def suggestFilename(self):
        count=0
        maxcount=3
        datestamp = datetime.date.today()
        datestamp = str(datestamp)
        tempname = "Convert7to8_" + datestamp + ".csv"
        while os.path.isfile(tempname) and count < maxcount:
            tempname = "Convert7to8_" + datestamp + "_" + str(count) + ".csv"
            print("suggested file name ", tempname)
            count +=1
        if count == maxcount:
            print("unable to suggest a filename")
            tempname=""
        else:
            print("final suggested filename ", tempname)    
        return(tempname)
    #end method suggestFilename
        
    def createFileYN(self, newfile='', emptyfile=''):
        """ Prompt user for permission to create file
            newfile is no file specified. emptyfile is a filename passed in via CLI   """
        if newfile:
            print("Program does not detect a filename. Would you like to use a csv file \
            to store data the program discovers, creates, or changes, other than the logfile?")
            print("Suggested filename is ", newfile)
        else:
            print(emptyfile, " is not an existing file.")
            
        createYN = input("Would you like the program to create it? Y/N ")
        return(createYN)

    #def chooseFileAndList():
    def noFileNoList(self):
        """ Prompt user because no Filename, no IP Address and No Testrouter   """
        iplist = []
        filename=''
        print("No filename and no IP address is detected by the program")
        choose=input("do you want to enter a filename (f) or a IP Address (ip)?")
        if choose == 'ip':
            iplist = input("please enter the ip address, or comma separated list of IPs.  ")
            choice = ("ip",iplist)
        elif choose == 'f' :
            filename =  input("please enter the csv filename with the ip addresses to be checked - ")
            choice = ("filename",filename)
        return(choice)


    def showmessage(self, message):
        print("Inside view-showmessage")   
        print(message) 

if __name__ == "__main__":
    print ("CLI view is main")
    testview = UserPrompts()
    # newname = testview.suggestFilename()
    # print("pwd is ", os.getcwd())
    # with open(newname , 'a') as outfile:
    #     outfile.write("testline \n")
    #testYN = testview.createFileYN(newfile=newname)
    #viewchoice = testview.noFileNoList()
    #print(viewchoice)
    testview.showmessage("this is a test message")
    