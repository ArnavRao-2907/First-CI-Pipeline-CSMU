def is_armstrong(number):
    n=number
    s=0
    if number < 0:
        return False
    elif number == 0:
        return True
    else:
        while(n>0):
            r=n%10
            p=r*r*r
            s=s+p
            n=n//10
        if s==number:
            return True
        else:
            return False

	
if __name__=="__main__":
    print(is_armstrong())
