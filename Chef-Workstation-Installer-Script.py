#!/usr/bin/python

import webbrowser #for web broswer to open
import subprocess #for bash commands to work in Python
import zipfile    #unzip module
import time       #module for time
import sys        #for the exit if error with input occurs

url = 'https://0.0.0.0' #Input your chef server IP

#To do the process manually just uncomment the line 11 & 23 then uncomment line 22
#url1 = 'http://downloads.chef.io/chef-dk/'

print """
	Hello there! This program is to help you install Chef DK.
	When prompted just enter yes or no for your answers.
"""

#set your answer 
ans1 = raw_input("Are you ready to continue? ") 
 
if ans1 == "yes":
	#webbrowser.open_new_tab(url1)
	subprocess.call(
	["sudo su && curl -L https://www.opscode.com/chef/install.sh | bash"], shell=True
	)
else:
	sys.exit("Not a valid input sorry!")

subprocess.call(["chef verify"], shell=True)

print """
	Now we will pull up the Chef Server UI.
	Sign in with your account credentials.
	Go to Administration, your Organization, then Starter Kit, Click 'Download Starter Kit'
"""
time.sleep(7) #Delays for 7 seconds
	
webbrowser.open_new_tab(url) #Pulls up our Chef Server

ans2 = raw_input("Are you ready to continue? ")

if ans2 == "yes":
	print "Cool now lets move your files and verify your install"
else:
	sys.exit("Not a valid input sorry!")
	
#Unzips your starter kit .zip and places in your Downloads
zip = zipfile.ZipFile('chef-starter.zip')
zip.extractall('')
zip.close()

#Moves the chef-repo to your home directory
subprocess.call(["sudo mv chef-repo $HOME "], shell=True)

#Grabs the SSL and puts it in .chef trusted_certs folder
subprocess.call(["cd / && cd ~/chef-repo && knife ssl fetch"], shell=True)

#Shows the list of all the nodes
subprocess.call(["cd ~/chef-repo && knife client list"], shell=True)

#The \033[1;35m prints color so this statements sticks out more remove the tags if you don't like the color
print """
	\033[1;35m
	Now the chef-repo should now be moved to your home directory.
	SSL cert for the server should now be in .chef/trusted_certs folder.
	You may see a Warning in yellow font but that is normal. 
	Additionally, you should see all of the nodes for chef as the output above.
	If you see all the above statements your Workstation is now set up!
	\033[1;m
"""
