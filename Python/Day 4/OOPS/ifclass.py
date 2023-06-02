class if_class:
    def if_pos_neg(self,num):
        if(num>=0):
            print(f"{num} is positive")
        else:
            print(f"{num} is negative")

    def if_even_odd(self,num):
        if(num%2==0):
            print(f"{num} is even")
        else:
            print(f"{num} is odd")

    def if_leap_year(self,num):
        if(num%100==0):
            if(num%400==0):
                print(f"{num} is a leap year")
            else:
                print(f"{num} is not a leap year")
        else:
            if(num%4==0):
                print(f"{num} is a leap year")
            else:
                print(f"{num} is not a leap year")

if_obj=if_class()
if_obj.if_pos_neg(-1)
if_obj.if_even_odd(25)
if_obj.if_leap_year(2004)