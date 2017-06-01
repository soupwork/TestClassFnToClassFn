#!/usr/bin/python
"""
    This is the main module
    I want to instantiate a class object from "simpleClass"
    I want to call a function in simpleclass from main.
    I want to call a function in main from simpleclass
    
"""

from SecondClass import SecondClass
 
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
    print("check dir")
    print(dir())
    print("check second class object")
    print(dir(secondObj))
    mainObj.testToTestClass()
    
    secondObj.checkmain()