#
#This is the CLI view. no GUI elements.
import getpass



class UserPrompts():
    def __init__(self):
        self.username = input("enter the username to authenticate to router/switch: ")
        print ("i am going to print out password for this test")
        self.pword=getpass.getpass("please enter password <hidden> :")

        print ("username is :", self.username)
        print("Password is ", self.pword)

    def getLoginID(self):
        return(self.username,self.pword)
        
    def createFileYN(filename):
        """ Prompt user for permission to create file   """
        print("Suggested filename is ", filename)
        createYN = input("Would you like the program to create it? Y/N ")
        return(createYN)


if __name__ == "__main__":
    print ("CLI view is main")
    getUID=LoginDetails()
    testloginID=getUID.setID()
    