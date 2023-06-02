def rev_string_decorator(func):
    def wrapper():
        val=func()
        temp=val
        t=val
        c=0
        while temp!=0:
            temp//=10
            c+=1
        sum=0
        while(t>0):
            sum+=(t%10)**c
            t//=10
        if sum==val:
            return(f"{val} is Armstrong number")
        else:
            return(f"{val} is not Armstrong number")
    return wrapper

@rev_string_decorator
def armstrong_no():
    return 153
print(armstrong_no())