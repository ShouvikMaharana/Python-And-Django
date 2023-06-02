#name="Shouvik"
#name=input("ENTER YOUR NAME: ")
#print("Hello",name)
#a=input("ENTER AN INPUT ")
#print(type(a)) #ALWAYS GIVES STR FOR INPUT
a=1
b=2
print("Before Swapping")
print("a:",a)
print("b:",b)

#logic1
"""
c=a+b
a=c-a
b=c-b
"""
#logic2
"""
c=a
a=b
b=c
"""
#logic3
a,b=b,a

print("After Swapping")
print("a:",a)
print("b:",b)