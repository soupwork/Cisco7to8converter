
==============================================================================
Doug's Cisco Password 7 to Secret 8 converter
===============================================================================

Description
===============================================================================
This program will convert a cisco password 7 (insecure) into a 
  cisco secret 8 (sha256)
This program will have two view interfaces, one Tkinter GUI and one CLI. 
  I want to have something easy for people to use, and something that can be 
  used from the Linux/Unix command line.  
This program will input a csv (data: hostname, IP Address, Username, password7)
This program will SSH to a router, and use that to generate the SHA256 secret8
The csv will have a space res'd for the secret 8
The program will add to the csv, (extra data elements: plaintext password and secret8. 
Saving plaintext password might be turned off in production, or be an option.
running the CLI program with only a "-p7 level7password" will return the plaintext password


	

How It Works
===============================================================================
The program decrypts the password7 using cisco7decrypt by Richard Strnad.
The way the program generates the password 8 is to ssh into a router, create a new
test-username with the option for password8, test the new password by ssh-ing back 
into the router to verify the new password8 works, then removing the test-username.
It may be possible to use this program with GNS3, instead of having a physical router.

What is Needed?
===============================================================================
This program requires install of Netmiko and Getpass
This program will use argparse for the CLI view
This program requires a Cisco Router or Switch with a ios that supports 
"encryption algorithm sha256"
It may be possible to use GNS3 as the device to create the SHA256 Hashes, which 
could then be manually pasted into a device. Or GNS3 could be used to test 
this program.

This program uses another program as a sub-program.
#cisco7decrypt
#by Richard Strnad
#2019 oct 26th -retrieved from
 https://github.com/richardstrnad/cisco7decrypt
#

Command Line Options/Flags
================================================================================
-p7 password7 > This will ignore all the other options, and decrypt the 
	password7 into plaintext and exit

-tr testrouter/sha-router > this option will pass in the IP address of the router
	used to generate the sha256 secret8 password. If a network is running Radius,
	the program will not be able to SSH into it to verify the sha256 is correct.
	If a GNS3 router is used, it will need to be set up separately, beyond the
	scope of my experience to support. If the target router is using local 
	authentication, it can be used to verify the sha256 secret8 password.
	
-gui >this flag will launch a Tkinter GUI (in the future) instead of running as a 
		command line utility
		
-log > this will create a log file "Convert7to8_Log_datetime"
	Plain Logging will save a copy of the lines that are added to the configuration
	verbose logging (verbose flag) will add all the steps in the log, and will 
	contain usernames and passwords
		
-logfile filename > same as log, but allows user to specify the filename to be used.		

-verbose >this flag will have the program display to the screen all the steps that 
	are being taken to create and save the passwords in the target system. This
	will display usernames and plaintext passwords.
		
-verify > this flag will ssh into the test router to verify the username/secret8
	combination are working.
		
-f filename > this option imports a csv file. The first row is headers (not data)
	If included, the second row will be used as the test router.
	this option can be used in two ways. If IP addresses are provided
	(below 2nd row) then the new usernames/passwords will be appended to the 
	bottom of the file.  If no ip addresses are specified, the program will go 
	through the IP addresses in the file and search for passwords and password 7's.
	
-ip IP Address > this option will let user set one or more IP Addresses. Each IP
	address will need to have its own -ip
	usage -ip 192.168.0.1 -ip 192.168.10.1 -ip 192.168.20.1 (this will have the 
		program ssh into each of these three devices.

Should I have an option to check and apply service password-encryption if it is
    missing?
Should I have an option to add a default username/password if missing?	

Sample Usage
===============================================================================
*find the plaintext for a given password 7

c:\> python main728.py -p7 13351601181B0B382F747B

*check a single router ip

c:\> python main728.py -ip 192.168.20.1
	
Author
================================================================================
Douglas J. Sheehan
Oct-Dec 2019

License and Copyright
================================================================================
This program is released under the BSD license. 
Copyright (c) 2019, Douglas J. Sheehan
All rights reserved.

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are met:

1. Redistributions of source code must retain the above copyright notice, this
   list of conditions and the following disclaimer.
2. Redistributions in binary form must reproduce the above copyright notice,
   this list of conditions and the following disclaimer in the documentation
   and/or other materials provided with the distribution.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR
ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
(INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND
ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
(INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

The views and conclusions contained in the software and documentation are those
of the authors and should not be interpreted as representing official policies,
either expressed or implied, of the <project name> project.


Examples
===============================================================================
An example beginning (unchanged) username configuration line:

the line to be changed

The end result
#
!My test usernames/passwords
username dougs.test view SCADAview password Test01Passwd

username Username01 priv 15 password Password01

username Username02 priv 15 password Password02

username Username03 priv 15 password Password03

username Username04 priv 15 password Password04

username Username05 priv 15 password Password05

username Username06 priv 15 password Password06

username Username07 priv 15 algorithm-type sha256 secret Password07

## after service password-encryption

!
username doug.sheehan privilege 15 secret 8 $8$6cFk1.H6SH83c.$R7fbS5LX68PT6PZoa/ZcIgS1ctmxw4pkajg/L/Ule/g

username dougs.test privilege 15 password 7 09784B1A0D5546220A1F173D2F

username Username01 privilege 15 password 7 053B071C325B411B1D5546

username Username02 privilege 15 password 7 097C4F1A0A1218000F5C56

username Username03 privilege 15 password 7 13351601181B0B382F747B

username Username04 privilege 15 password 7 12290404011C03162E7B70

username Username05 privilege 15 password 7 08114D5D1A0E0A05165B59

username Username06 privilege 15 password 7 107E080A16001D1908547C

username Username07 privilege 15 secret 8 $8$F/w85a6wmpTYZk$ZQOonJGorZG9GMhX2eMUtChZmumf/wWRglqt8XFUUOk

!

# My Folder Structure

\CONVERT728

│   main728.py

│   README.rst

│   __init__.py

│

└───convert7to8PKG

    │   cisco7decrypt.py
    
    │   controller728.py
    
    │   model728.py
    
    │   view728.py
    
    │   view728CLI.py
    
    └─  __init__.py
    
     

Other Thoughts
===============================================================================
In learning about MVC architecture, I have come to understand that while all the 
different sections (Model-View-Controller) are built into separate .py files, 
they are all imported, executed, and managed by the one main module. The View 
is written separately, but the main program imports the view and runs the 
methods as if they were written inside the main program.

The CLI View will have the argpars parts and getpass. The view will pass those
to the controller, which will open the netmiko connections

Network Object Class 
[index][hostname][ip address][log][verbose]

	[orig username][test username][password 7][plaintext][secret 8][notes and errors]
	
Network Object is the basic data object for my program. Hostname should be unique in a network.
            Hostname is manditory. IP is manditory. A hostname can have multiple IP's, but an IP can only 
            be assigned to one hostname. Log and verbose are optional. Login username and password for the 
            device (IP) are handled by the main program and never saved to a file. A network object might not 
            have any password 7's, in which case "No Password 7" will be in the notes field.
			Each network object will have a numerical index, for sorting in the future. 


Endnote
================================================================================
What is this world coming to? my readme is over 200 lines? Who wants to spend that
time reading about this? Hopefully the program is shorter and more 
self-explanatory and nobody will need to open this up.

If I had known how long this program was going to take me, I probably would have 
gone looking for a less intensive hobby. Of the things that are taking a lot of 
time, worthy of note is learning new things, learning things I had learned before
and was sure that I had understood and mastered, going to ridiculous extremes to make
sure the program is operating exactly as expected, and a multitude of test datum
being sent to individual modules and functions before testing the main program, and 
testing the integration of all elements through the main program. I'll also add thinking.
I've done a lot of thinking, pondering, considering, what the best or most correct way,
or what will be the easiest for someone to help with troubleshooting.
