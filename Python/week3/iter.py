my_tuple = ("apple", "banana", "cherry")
my_iter = iter(my_tuple)

print(next(my_iter))
print(next(my_iter))
print(next(my_iter))

class MyNumbers :
    def iter ( self) :
        self.a = 1
        return self
    def __next__ ( self) :
        if self.a <= 20 :
            x = self.a
            self.a += 1
            return x
        else :
            raise StopIteration

myclass = MyNumbers()
myiter = iter(myclass)
iter (myclass )
print ( next (myiter) )
print ( next (myiter) )
print ( next (myiter) )
print ( next (myiter) )
print ( next (myiter) )