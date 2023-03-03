class Solve():
    #def __init__(self, s1, s2, s3):
    #    self.s1 = s1
    #    self.s2 = s2
    #    self.s3 = s3
        
    def rectangle(self, s1, s2, s3):
        if s1 != 0 and s3 != 0 and s2 == 0:
            return (int(s1) + int(s3)) *2
        if s1 != 0 and s2 != 0 and s3 == 0:
            return (int(s1) + int(s2)) *2
        if s3 != 0 and s2 != 0 and s1 == 0:
            return (int(s2) + int(s3)) * 2
    
    def triangle(self, s1, s2, s3):
        if s1 and s2 and s3 != 0:
            return int(s1) + int(s2) + int(s3)
         
    def square(self, s1, s2, s3):
        if s1 == 0 and s2 == 0:
            return int(s3)*4
        if s2 == 0 and s3 == 0:
            return int(s1) *4
        if s1 == 0 and s3 == 0:
            return int(s2) *4

default = 0
s1= input("First side: ") or default
s2= input("Second side: ") or default
s3= input("Third side: ") or default

per = Solve()

print("The rectangle's perimeter is: {}".format(per.rectangle(s1, s2, s3)))
print("The triangle's perimeter is: {}".format(per.triangle(s1, s2, s3)))
print("The square's perimeter is: {}".format(per.square(s1, s2, s3)))

#def square(self):
#    if self.s1 and self.s2 == " ":
#        return self.s3 * 4
#    if self.s2  and self.s3== " ":
#        return self.s1 * 4
#    if self.s3 and self.s3 == " ":
#        return self.s2 * 4
#print("The square's perimeter is: " + square)

#for s1,s2,s3 in ()
        

#class userInput(self, s1, s2, s3):
#
#    s1= float(input("First side: "))
#    s2= float(input("Second side: "))
#    s3= float(input("Third side: "))
#        
#    class triangle(userInput):
#        def perimeterSquare(self, s1):
#            return (s1**2)
#        print("The triangle's perimeter is: }" + triangle)
#    
#    class square(userInput):
#        def perimeterSquare(self, s1):
#            return (s1**2)
#    
#    
#    print("The square's perimeter is: " + square)
#    
#    
#    class rectangle(userInput):
#        def perimeterRectangle(self, s1, s2):
#            return ((s1+s2)*2)
#    
#    print("The rectangle's perimeter is: " + rectangle)
