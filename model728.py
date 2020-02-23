#This is my Model. This is the Data. These are the methods that act direct on the data.
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



class NetworkObject:
    """Network object will have 'HOSTNAME','IPADDRESS','LOG','VERBOSE','ORIGUSERNAME','TESTUSERNAME', \
            'PASSWORD7','PLAINTEXT','SECRET8','CHANGE','VERIFIED','NOTES-AND-ERRORS'
        """ 

    def __init__ (self, netobjDict):
        """Network Object is the basic data object for this program. Hostname should be unique in a network.
            Hostname is manditory. IP is manditory. A hostname can have multiple IP's, but an IP can only 
            be assigned to one hostname. Log and verbose are optional. Login username and password for the 
            device (IP) are handled by the main program and never saved to a file. A network object might not 
            have any password 7's, in which case "No Password 7" will be in the notes field."""
            
        self.netobjDict=netobjDict
        print("IP Address is ",self.netobjDict['IPADDRESS'])
        print("Verbose messages is ", self.netobjDict['VERBOSE'])
        print("Log messages is ", self.netobjDict['LOG'])
        print("Username is ", self.netobjDict['ORIGUSERNAME'])
    def checkUsername(self, username):
        pass
    
    def addUsername(self, username):
        pass

    def prepareUsernameCommand(self):
        self.netobjDict[TESTUSERNAME] = self.netobjDict[',ORIGUSERNAME'] + '_TEST'
        usernamecommand = 'username {0} algorithm-type sha256 secret {1}' \
            .format(self.netobjDict['ORIGUSERNAME'],self.netobjDict['PLAINTEXT'] )
        testusernamecommand = 'username {0} priv 15 algorithm-type sha256 secret {1}' \
            .format(self.netobjDict['TESTUSERNAME'],self.netobjDict['PLAINTEXT'] )

        print(testusernamecommand, " \n to be used on testrouter")
        return(testusernamecommand)
        # username newuser privilege 15 algorithm-type sha256 secret plaintext  
        # username {} priv 15 algorithm-type sha256 secret {}    




    def showPass7(self):
        return(self.netobjDict['PASSWORD7'])

    def setPlaintext(self, plaintext):    
        self.netobjDict['PLAINTEXT'] = plaintext

    def showPlaintext(self):
        return(self.netobjDict['PLAINTEXT'])


class NetworkObjectGroup:
    """main instantiates Network Object Group Object (netobjgroup)
    input needs initial dictionary, from InitializeModel (passed through main)
    Create list with up to max_elements from filename. Find length of file.
    create pointer for list, create pointer for file if longer than 500 rows
    load next 500 rows if needed
    keep track of updates to plaintext, secret 8, notes, etc.
    update log/verbose if selected.
    """
    max_elements = 1024

    def __init__(self, initDict):
        """
         initial dictionary from main(this is objDict from init.model). 
          create list of up to max_elements rows from filename. create pointer for list
          return dict with new row data.
        """

        self.netObjCount = 0
        self.ipindex=0
        self.iplist = initDict['IPADDRESS']
        self.netObjList=[]

    
         #   print("Network Object will be ", "netobj_" + self.netObjCount)

            #now i need to ssh into ip address and find out how many usernames are there.

    def createNetObjs(self,netObjDict):
        pass
               
    def getNextIP(self): 
        if self.ipindex < len(self.iplist):
            nextIP = self.iplist[self.ipindex]   
            self.ipindex +=1
            print("next IP Address is ", nextIP)
        else: 
            nextIP=''    
            print("no more IP's")
        return(nextIP)
         

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
    

    def __init__(self, cliDict):
        """init prepares the default dict and details file"""

        print("initializing Model")
        #self.filename = filename
        #print("filename is ",self.filename)
        self.cliDict=cliDict
        self.objdict = {'HOSTNAME':'','IPADDRESS':'','LOG':'','VERBOSE':'','ORIGUSERNAME':'','TESTUSERNAME':'', \
            'PASSWORD7':'','PLAINTEXT':'','SECRET8':'','CHANGE':'','VERIFIED':'','NOTES-AND-ERRORS':''} 
        #testing
        #self.path = 'e:/dougsprogs/convert7to8/convert728/'
        

        ##Main checks to see if Filename is blank
        #if filename :#filename is not blank.
            #self.checkFilename()
        #if filename is blank, create the default dict
        #else: #filename is blank ""
        self.loadDictRow()
            #loadDictValue(key="IPADDRESS", value=str(ipaddress))
            #now check to create the default empty file
            #checkFilename()
 
  
    def loadDictRow(self, valuestring=""):
        
        
        #if valuestring is not blank, load values in objDict
        if valuestring:
            valuestring = valuestring.upper()
            valuestring = valuestring.strip()
            valuestring = valuestring.replace(" ","") #remove internal spaces
            valuestring=valuestring.split(',')
            #add values to the  Dictionary
                        
            index = 0

            for key in self.objdict:
                
                self.objdict[key]= valuestring[index]
                index += 1
            #end for loop through dict keys
        else: 
            for key in self.objdict:
                if key in self.cliDict:
                    self.objdict[key] = self.cliDict[key]
                    print("assigned key/value ", key, " ", self.objdict[key])
   
    def getHeaderDict(self):
        """
        Make sure headers in filenname are correct. create a dict to pass back to main.
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
           # elif (miscount == 11) and ("IPADDRESS" in ):
           #     print("Found IP Address column. program will add additional columns")
            elif miscount > 11:
                print("Could not locate Header Row")
            elif miscount > 0:
                print("some columns missing, will add additional columns")
            
         
        #end file check on filename    

    def loadMaxIPlist(self, filename):
        """this will load up to first 500 ip's into dict-ip address list and give a count of number
            of ip addresses in list"""
        #I need to put this in a try/catch block later   
        
        maxIPlist=10
        linecount=0    
        iplist=[]
        with open(filename, 'r') as infile:
            element = infile.readline()
            while element:
                
                linecount +=1
                if linecount < maxIPlist:
                    iplist.append(element)
                element = infile.readline()
 
        self.objdict['IPADDRESS']=iplist
        print("Loaded ", linecount, " ip addresses")

        return(linecount)        

    def checkFilename(self):
        """don't create the network object group until filename is checked
            is there a special path?
            does file exist? 
            does file have expected headers?
            is second row the test router?
            how many rows is the file? can I load in memory or take it in chunks?
        """
        
        #all this should be in the view

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
    #end method checkFilename  

   

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
    #end method createFile
      
#End Class InitializeModel


if __name__ == "__main__":
    print("starting from model")
    testfilename = "testIPlist2.csv"
    #testfilename="e:/dougsprogs/Convert728/convert7to8PKG/testdata728.csv"
    #testfilename="e:\dougsprogs\Convert728\convert7to8PKG\\testdata728.csv"
    #testfilename="testdata728.csv"  #this is a real file with some data
    #testfilename="testblank728.csv"  #this is a real file with no data
    #testfilename="testempty728.csv" #this is not an existing file
    #testfilename=""                 #this is an empty filename
    #dataobject=convert_model(testfilename)
    #password7="111918160405041E007A7A"
    #plaintext=dataobject.decrypt(password7)
    #print("plaintext is ",plaintext)
    #testobj=NetworkObject(ip="192.168.20.1", verbose=True)
    #checkthis=InitializeModel(testfilename)
    #checkthis.checkFilename()
    #tempDict = checkthis.retObjDict()
    # testobj = NetworkObjectGroup(filename = "")

    #2020 feb 1st testing  Network Objects
    testdict = {'HOSTNAME':'testhostname','IPADDRESS':'192.168.20.1','LOG':'n','VERBOSE':'n','ORIGUSERNAME':
    'Username01','TESTUSERNAME':'', 'PASSWORD7':'053B071C325B411B1D5546','PLAINTEXT':'','SECRET8':'','CHANGE':'y','VERIFIED':'','NOTES-AND-ERRORS':''}
    newmodel = InitializeModel(testdict)
    linecount = newmodel.loadMaxIPlist(testfilename)
    print("linecount is ",linecount)
    for ip in newmodel.objdict['IPADDRESS']:
        print("IP Address is ", ip)