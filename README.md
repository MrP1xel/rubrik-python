# rubrik-python
How to connect to Rubrik API with python

The rubrik_wrapper.py is a simple wrapper to the Rubrik API , used by functions implemented into the rubrik.py script

The rubrik.py contains functions to ease the usage of rubrik API 


# How to connect to your rubrik with python


``` python
#import the rubrik.py files
import rubrik

#create a Session object with your rubrik credentials
mySession = Session("admin","mmmm")

#Create a Cluster object with the IP of your rubrik and the Session object created just above
rubrik_test = Cluster("127.0.0.1",mySession)

#Main loop of your script
#The .auth() method return True if connection is OK, else False

if rubrik_test.auth():
  print getVersion(Cluster)
else:
  print "connection issue"


``` 
That's all, you must be connected to your rubrik in just 3 lines of python 



