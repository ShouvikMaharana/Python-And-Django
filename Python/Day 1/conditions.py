#a=int(input("Enter a number"))
#if(a%2==0):
  #  print(f"{a} is Even")
#else:
   # print(f"{a} is Odd")

a=int(input("Enter a year"))
if(a%100==0):
    if(a%400==0):
        print(f"{a} is a leap year")
    else:
        print(f"{a} is not a leap year")
else:
    if(a%4==0):
        print(f"{a} is a leap year")
    else:
        print(f"{a} is not a leap year")