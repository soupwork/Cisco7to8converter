#
#This is the CLI view. no GUI elements.
import getpass
import datetime
import os.path


class UserPrompts:
    def __init__(self):
        self.username = input("enter the username to authenticate to router/switch: ")
        self.pword=getpass.getpass("please enter password <hidden> :")
        print ("username is :", self.username)

    def getLoginID(self):
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


if __name__ == "__main__":
    print ("CLI view is main")
    testview = UserPrompts()
    newname = testview.suggestFilename()
    print("pwd is ", os.getcwd())
    with open(newname , 'a') as outfile:
        outfile.write("testline \n")
    #testYN = testview.createFileYN(newfile=newname)
    