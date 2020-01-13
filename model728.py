#This is my Model. This is the Data.
#There will be three classes. 
# the will be a Log7to8, which keeps track of what the program is doing
# there will be a NetworkObject class, which is a Hostname, IP, 
#    and a list of Usernames with privledge level, password7, plaintext, secret8
#There will be a NetworkObjectGroup- do i need a class for this? it is really a list of
#   network Objects and file operations, maybe sorting.
#
import datetime
import os.path

#from convert7to8PKG.cisco7decrypt import decode

def changeDict(self, tempDict, keystring="", valuestring=""):
    
        #if keystring is not blank, load keys in loadDict
        if keystring:
            keystring = keystring.upper()
            keystring = keystring.strip()
            keystring = keystring.replace(" ","") #remove internal spaces
            #add values to the  Dictionary
            keylist=keystring.split(',')
            
            for key in keylist:
                tempDict[key] = ""
                        
        
        #if valuestring is not blank, load values in tempDict
        if valuestring:
            valuestring = valuestring.upper()
            valuestring = valuestring.strip()
            valuestring = valuestring.replace(" ","") #remove internal spaces
            #add values to the  Dictionary
            valuelist=valuestring.split(',')
            index = 0

            for key in tempDict:
                tempDict[key]= valuelist[index]
                index += 1
        #end for loop through dict keys    

def suggestFilename():
    datestamp = datetime.date.today()
    tempname = "Convert7to8_" + str(datestamp) + ".csv"
    return(tempname)

class NetworkObject():
    """Network object will have [index][hostname][ip address][log][verbose]
	[orig username][test username][password 7][plaintext][secret 8][notes and errors]
        """ 

    def __init__ (self, netobjDict):
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
    """main instantiates Network Object Group Object (NetObjGroup)
    input needs initial dictionary, and filename/
    Create list with up to 500 elements from filename. Find length of file.
    create pointer for list, create pointer for file if longer than 500 rows
    load next 500 rows if needed
    keep track of updates to plaintext, secret 8, notes, etc.
    update log/verbose if selected.
    """
    def __init__(self, filename, initDict, ip=""):
        """
          init needs a filename and the initial dictionary. 
          create list of up to 500 rows from filename. create pointer for list
          return dict with new row data.
        """

        self.filename = filename
        print("filename is ",filename)
        self.workingDict = initDict
        self.workingList = [] #working list will be all the elements 
        self.iplist = [] #ip list is only ip addresses
        self.rowcount = 0
        self.rowpointer
        maxlines = 500 # maximum number of lines in the working list
        
        
        #blah. I need to check if ip addresses are passed in to take priority over filenames.
        # Change for this will start in Main
        # if self.filename:  #filename is not blank
        #     with open(self.filename, 'r') as readfile:
        #         rowstring = readfile.readline() #first read should be the headers
        #         while rowstring : #rowstring will be -1 at the end of the file
        #             rowstring = readfile.readline() #rowstring false(-1) when line is blank
        #             rowcount += 1
        #             if rowstring and (rowcount < maxlines):
        #                 self.workinglist.append(rowstring)
        #                 print("new list entry ", rowstring)
        # else:   #filename is blank
        #     self.iplist=ip

        #load first IP (test router) into the dict.

                     
              

           

    def nextRow(self):
        """ this will load the next row into the workingDict and pass back to main"""
        pass


    

class Logmessages():
    """
        timestamp = datetime()
        timestamp = datetime.now()
        print ("timestamp is ", timestamp.now())
    """
    pass
    


class InitializeModel():
    """ This class sets up the model. 
        Other Classes in the Model are Logmessages, Network Object, and Network Object Group
    """
    

    def __init__(self, filename, path="", ipaddress=""):
        """init filechecks just needs the filename"""

        print("initializing Model")
        self.filename = filename
        print("filename is ",self.filename)
        self.path = path
        self.objdict = {} #create an empty dictionary for headers/values
        #testing
        #self.path = 'e:/dougsprogs/convert7to8/convert728/'
        #dataheader is a tuple - immutable
        self.dataheader = ('HOSTNAME','IPADDRESS','LOG','VERBOSE','ORIGUSERNAME','TESTUSERNAME', \
            'PASSWORD7','PLAINTEXT','SECRET8','CHANGE','VERIFIED','NOTES-AND-ERRORS')

        print("data headers should be ", self.dataheader)
        #if filename is blank, create the default dict
        if not filename: #filename is blank ""
            headerstring = str(self.dataheader)
            self.loadDictRow(keystring = headerstring)
            #loadDictValue(key="IPADDRESS", value=str(ipaddress))
            #now check to create the default empty file
            #checkFilename()
        else: #filename is not blank.
            pass    
    
    def retObjDict(self):
        """this method will pass the blank or test router dictionary
            back to the main to create a Network Object """
        print("return default dictionary is ", self.objdict)
        return(self.objdict)

    def createFile(self):
        print ("this will create a file ", self.filename)
        print ("headers will be ", self.dataheader)
        writestring = ""
   
        for element in self.dataheader:
            writestring = writestring + str(element) + ","

        writestring=writestring[:-1] + '\n'   
        print("default working directory is ", os.getcwd())
        print("current working directory is ", self.path)
        print("writestring is ", writestring)
        with open(self.filename, 'a') as outfile:
            outfile.write(writestring)

    def loadDictRow(self, keystring="", valuestring=""):
        
        #if keystring is not blank, load keys in loadDict
        if keystring:
            keystring = keystring.upper()
            keystring = keystring.strip()
            keystring = keystring.replace(" ","") #remove internal spaces
            #add values to the  Dictionary
            keylist=keystring.split(',')
            for key in keylist:
                self.objdict[key] = ""
                        
        
        #if valuestring is not blank, load values in objDict
        if valuestring:
            valuestring = valuestring.upper()
            valuestring = valuestring.strip()
            valuestring = valuestring.replace(" ","") #remove internal spaces
            valuestring=valuestring.split(',')
            #add values to the  Dictionary
                        
            index = 0

            for key in self.objdict:
                
                self.objdict[key]= valuelist[index]
                index += 1
            #end for loop through dict keys
 
    def loadDictValue(self, key, value):
        self.objdict[key]=value
        print("set value in Dict ", key, ": ", value)
                

    def getHeaderDict(self):
        """
        Make sure headers are correct. create a dict to pass back to main.
        """
      
        #put the headers into a dict
        
        print("opening ",self.filename)
        with open(self.filename, 'r') as readfile:
            headers = readfile.readline()
            firstrow = readfile.readline()
            if not firstrow:
                print("first line after headers is blank")
                self.loadDictRow(keystring=headers)
            else: #assume first row after headers is test router
                print("load test router row") 
                self.loadDictRow(keystring = headers, valuestring = firstrow)            
              
          
            # check for headers
            miscount=0
            for key in self.dataheader:
                if not key in self.objdict:
                    print("missing key !", key)
                    miscount += 1

            if miscount == 0:
                print("all Columns found. Thank you.")
            elif (miscount == 11) and ("IPADDRESS" in headerdict):
                print("Found IP Address column. program will add additional columns")
            elif miscount > 11:
                print("Could not locate Header Row")
            elif miscount > 0:
                print("some columns missing, will add additional columns")
            
         
        #end file check on filename    



    def checkFilename(self, path=""):
        """don't create the network object group until filename is checked
            is there a special path?
            does file exist? 
            does file have expected headers?
            is second row the test router?
            how many rows is the file? can I load in memory or take it in chunks?
        """
        
        #testing
        #self.path = 'e:/dougsprogs/convert7to8/convert728/'

        if self.filename == "":
           pass            # createFile(self.filename)

        elif self.filename.find('/') or self.filename.find('\\'):
            print("slashes in the filename mean path is included")
        elif self.path == "":
            self.path = os.getcwd()
            elf.filename = self.path + self.filename
        elif path.endswith("/"):
            self.filename = self.path + self.filename
            print("entire filename/path is ", self.filename)
        # else:
        #     self.filename = str(path) + "/" + self.filename   y 

        print("working directory ", self.path) 
        print("If you'd like to use another directory/folder, please include the full path with the filename.")
        #should i let users change working directory or just put it in the file path
        print("checking filename ", self.filename)
        
        

        if not os.path.isfile(self.filename):
            print("this is not an existing file")
            createYN = (input("create it? y/n ")).upper()
            if createYN=='Y':
                self.createFile()
                self.getHeaderDict()

            else: # create file = NO
                headerDict = {}    #create an empty dictionary
                self.loadDictRow(keystring = '') #this will create keys but not values

        else:
            """
            Check to see if the first row is headers, and second row is Test Router
            """
            print("this is an existing file")
            self.getHeaderDict()



if __name__ == "__main__":
    print("starting from model")
    
    #testfilename="e:/dougsprogs/Convert728/convert7to8PKG/testdata728.csv"
    #testfilename="e:\dougsprogs\Convert728\convert7to8PKG\\testdata728.csv"
    #testfilename="testdata728.csv"  #this is a real file with some data
    #testfilename="testblank728.csv"  #this is a real file with no data
    #testfilename="testempty728.csv" #this is not an existing file
    testfilename=""                 #this is an empty filename
    #dataobject=convert_model(testfilename)
    #password7="111918160405041E007A7A"
    #plaintext=dataobject.decrypt(password7)
    #print("plaintext is ",plaintext)
    #testobj=NetworkObject(ip="192.168.20.1", verbose=True)
    checkthis=InitializeModel(testfilename)
    checkthis.checkFilename()
    tempDict = checkthis.retObjDict()
    # testobj = NetworkObjectGroup(filename = "")