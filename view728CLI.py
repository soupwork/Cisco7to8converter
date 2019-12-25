#
#This is the CLI view. no GUI elements.
import getpass

    

class LoginDetails():
    def __init__(self):
        self.username = input("enter the username to authenticate to router/switch: ")
        print ("i am going to print out password for this test")
        self.pword=getpass.getpass("please enter password <hidden> :")

        print ("username is :", self.username)
        print("Password is ", self.pword)

    def getLoginID(self):
        return(self.username,self.pword)



if __name__ == "__main__":
    print ("CLI view is main")
    getUID=LoginDetails()
    testloginID=getUID.setID()
    