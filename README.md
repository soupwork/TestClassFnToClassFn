# TestClassFnToClassFn
test calling from one class object function to another class object function in python 3

Reading other people’s code is hard. I’ll try to keep it short. 

I am trying to call a function in an instantiated class from a function in another instantiated class.

I’ve reduced my code to the bare minimum to try to make it a little easier.

Originally, I was trying to call a function in main *from* a method in an instantiated object.
It didn't work. I tried for a few days to find a way with no luck. My workaround was to make a new class and try to call the function in the class. It isn't working for me either. 

I've renamed the files .txt in case something gets flagged by security stuff.

Some of the possible solutions that I found on stack overflow and in my reading are
  Inheritance/call to Super() methods
  Delegation
  bound/unbound methods
  
I susupect there may be something with namespaces that will be a workaround.
I don't think what I'm trying to do should be unusual or difficult. Maybe there are some OOP concepts that I am not understanding. I am sure I am getting closer. 

I have two files. One is a package that I import into the main module. the other is the main module. 
I can call *from* the class function in main *to* the class function in imported class(simpleClass) but the same syntax is not working going back the other way. I am getting a "NameError: name 'MainClass' is not defined"
