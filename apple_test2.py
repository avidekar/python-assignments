class A(object):
    def go(self):
        print("go A go!")
    def stop(self):
        print("stop A stop!")
    def pause(self):
        raise Exception("Not Implemented")

class B(A):
    def go(self):
        super(B, self).go()
        print("go B go!")

class C(A):
    def go(self):
        super(C, self).go()
        print("go C go!")
    def stop(self):
        super(C, self).stop()
        print("stop C stop!")

class D(C,B):
    def go(self):
        super(D, self).go()
        print("go D go!")
    def stop(self):
        super(D, self).stop()
        print("stop D stop!")
    def pause(self):
        print("wait D wait!")

class E(B,C): pass

a = A()
b = B()
c = C()
d = D()
e = E()

# specify output from here onwards

a.go() # go A go!
print("-")
b.go() # go A go! \n go B go!
print("-")
c.go() # go A go! \n go C go!
print("-")
d.go() # go A go! \n go B go! go A go! \n go C go! \n go D go!
print("-")
e.go() # go A go! \n go B go! go A go! \n go C go!
print("-")

a.stop() # stop A stop!
print("-")
b.stop() # stop A stop!
print("-")
c.stop() # stop A stop! \n stop C stop!
print("-")
d.stop() # stop A stop! \n stop A stop! \n stop C stop! \n stop D stop!
print("-")
e.stop() # stop A stop! \n stop A stop! \n stop C stop!
print("-")

a.pause() # exception thrown. print -> Not Implemented
# b.pause() # exception thrown. print -> Not Implemented
# c.pause() # exception thrown. print -> Not Implemented
# d.pause() # wait D wait!
# e.pause() # exception thrown. print -> Not Implemented
