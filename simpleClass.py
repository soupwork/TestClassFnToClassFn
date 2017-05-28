#!/usr/bin/python
"""
    This is a simple class
    
"""


class SimpleClass: #

    #the name of the object in main is mainObj
    #the name of this object in main is simpleObj
    def __init__(self, maine="not main"):

        self.maine=maine
        print("mainObj is ", maine)
        print("name in SimpleClass init is ", __name__)
        
    def testfn(self):
        print("this is a testfn. it is only a test")
        
        
    def checkmain(self):
        print("checkmain in simpleclass ", self.maine)
        print("calling back to main")
        MainClass.testFnInMain(mainObj)
        print("MainClass.testFnInMain(mainObj)")#I need this line to work.
        #calling Classname.functionname(objname) is what i really need to do. :(
        #I need to call the function in mainclass from a package that I'm importing.
        
if __name__=="__main__":

    print("running __main__ in Simple Class 2017 may 22nd")
    simpleObj = SimpleClass(maine=maine) #
    simpleObj.testfn()
