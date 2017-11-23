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

#Call the auth() method of the Cluster object
rubrik_test.auth()

``` 
That's all, you must be connected to your rubrik in just 4 lines of python 



