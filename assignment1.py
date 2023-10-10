#area of circle
r=float(input("enter the radius of circle:"))
area=3.14*r*r
print("area of the circle is:",area)
#extension of file
filenam=str(input("enter file name:"))
extension=filenam.split(".")
print("extension of file is:",repr(extension[-1]))

