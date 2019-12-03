# Cisco7to8converter
this is python gui and cli project to convert password 7's (insecure) to password 8's (SHA-256)
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
This program will optionally input a csv (data: hostname, IP Address, Username, password7)
This program will SSH to a router, and use that to generate the SHA256 secret8
The csv will have a space res'd for the secret 8
The program will add to the csv, (extra data elements: plaintext password and secret8. 
Saving plaintext password might be turned off in production, or be an option.

How It Works
===============================================================================
The program decrypts the password7 using cisco7decrypt by Richard Strnad.
The way the program generates the password 8 is to ssh into a router, create a new
test-username with the option for password8, test the new password by ssh-ing back 
into the router to verify the new password8 works, then removing the test-username.

What is Needed?
===============================================================================
This program requires install of Netmiko and Getpass
This program will use argparse for the CLI view
This program requires a Cisco Router or Switch with a ios that supports 
"encryption algorithm sha256"

This program uses another program as a sub-program.
#cisco7decrypt
#by Richard Strnad
#2019 oct 26th -retrieved from
# https://github.com/richardstrnad/cisco7decrypt
#


Examples
===============================================================================
An example beginning (unchanged) username configuration line:

the line to be changed

The end result

Other Thoughts
===============================================================================
In learning about MVC architecture, I have come to understand that while all the 
different sections (Model-View-Controller) are built into separate .py files, 
they are all imported, executed, and managed by the one main module. The View 
is written separately, but the main program imports the view and runs the 
methods as if they were written inside the main program.

Author
================================================================================
Douglas J. Sheehan


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

Endnote
================================================================================

#
#
My test usernames/passwords
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
Folder Structure
\CONVERT728\
│   728main.py
│   README.rst
│   TestImports.py
│   TestNetmiko.py
│   __init__.py
│
└──\convert7to8
    │   728controller.py
    │   728data.csv
    │   728model.py
    │   728GUIview.py
    │   728CLIview.py
    │   cisco7decrypt.py
    │   cisco7decrypt2.py
    │   testdata728.csv
    │   testdataprep-728.txt
    │   view728.py
    │   __init__.py
    
