#!/usr/bin/python
"""
    This is the main module
    I want to instantiate a class object from "simpleClass"
    I want to call a function in simpleclass from main.
    I want to call a function in main from simpleclass
    
"""

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
        simpleMain.MainClass.testFnInMain(mainObj) 
        
        
class MainClass:   

    def __init__(self,name):
        print("MainClass name is", __name__)
        self.name=name
        print("MainClass name is", self.name)
    
    def testFnInMain(self):
        print("this is the test function in main")
        
    def testToTestClass(self):
        print("begin: calling test function in second Class")
        SecondClass.testfn(secondObj) #
        print("end: calling test function in second Class")
# end MaineClass   
    

if __name__=="__main__":
    """This is my main program.  """
    maine="testname"
    print("the name of main in simpleMain is ", maine)
    mainObj=MainClass(maine)
    secondObj=SecondClass()

    mainObj.testToTestClass()
    secondObj.checkmain()