#!/usr/bin/python
"""
    This is a simple class
    
"""
#import simpleMain

class SecondClass: #

    #the name of the object in main is mainObj
    #the name of this object in main is simpleObj
    def __init__(self, maine="not main"):
        print("name in SecondClass init is ", __name__)
        
    def testfn(self):
        print("this is a second class testfn. it is only a test")
        print(dir(self))
        
    def checkmain(self):
    
        print("calling back to main")
        #simpleMain.MainClass.testFnInMain(mainObj)
 
