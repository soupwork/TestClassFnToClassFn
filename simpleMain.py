#!/usr/bin/python
"""
    This is the main module
    I want to instantiate a class object from "simpleClass"
    I want to call a function in simpleclass from main.
    I want to call a function in main from simpleclass
    
"""

from simpleClass import SimpleClass
 
class MainClass:   

    def __init__(self,name):
        print("MainClass name is", __name__)
        self.name=name
        print("MainClass name is", self.name)
    
    def testFnInMain(self):
        print("this is the test function in main")
        
    def testToTestClass(self):
        print("begin: calling test function in simple Class")
        SimpleClass.testfn(simpleObj) #this call works
        print("end: calling test function in simple Class")
# end MaineClass   
    

if __name__=="__main__":
    """This is my main program.  """
    maine=__name__
    print("the name of main in simpleMain is ", maine)
    mainObj=MainClass(maine)
     
    simpleObj=SimpleClass()

    mainObj.testToTestClass()
    print("\n", MainClass.__dict__, "\n ")
    print(mainObj.__dict__,"\n ")
    print(SimpleClass.__dict__,"\n ")
    print(simpleObj.__dict__)
    simpleObj.checkmain()