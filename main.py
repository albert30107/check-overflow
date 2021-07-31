INT_MAX=2147483647
INT_MIN=-2147483648

times=1

check_number=eval(input("input number to check:"))

if check_number*times>INT_MAX:
    print(check_number*times,"is overflow: ",check_number*times%INT_MAX-1+INT_MIN)
elif check_number*times<INT_MIN:
    print(check_number*times,"is overflow: ",INT_MAX+check_number*times-INT_MIN+1)
else:
    print(check_number*times,"not overflow")
