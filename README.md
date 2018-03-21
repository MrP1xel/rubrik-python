# rubrik-python
How to connect to Rubrik API with python

The rubrik_wrapper.py is a simple wrapper to the Rubrik API , used by functions implemented into the rubrik.py script

The rubrik.py contains functions to ease the usage of rubrik API 


# How to connect to your rubrik with python


``` python
#import the rubrik.py files
from rubrik import *

#create a Session object with your rubrik credentials and the IP
mySession = Session("admin","mmmm",IP_of_rubrik)


#Main loop of your script
#The .auth() method return True if connection is OK, else False

if mySession.auth():
  print getVersion(mySession)
else:
  print "connection issue"


``` 
That's all, you must be connected to your rubrik in just 3 lines of python 



