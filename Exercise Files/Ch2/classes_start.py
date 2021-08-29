#
# Example file for working with classes
#
class myclass():
    def method1(self):
        print("my class method1")

    def method2(self, someString):
        print("my class method2 " + someString)
class anotherClass(myclass):
    def method1(self):
        myclass.method1(self)
        
        print("another class method1")

    def method2(self, someString):
        print("another class method2")

def main():
   c = myclass()
   c.method1()
   c.method2("This is a string")
   c2=anotherClass()
   c2.method1()
   c2.method2("This is a string")
   # First I'm going to call the inherited method from the superclass
   #which is method1() in myClass()
   # to do that write this code in anotherClass() definition
   #myclass.method1(self)

 
if __name__ == "__main__":
    main()
