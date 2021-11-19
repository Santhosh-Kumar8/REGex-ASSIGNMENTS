# TASK 1

# SANTHOSH KUMAR J

# 1)

##n = 5
##for i in range(5):
##    for j in range(n - i):
##        print("5",end = " ")
##    print()

# 2)

##rows = 5
##for i in range(rows,0,-1):
##    for j in range(0,i+1):
##        print(j,end = " ")
##    print()

# 3)

##rows = 5
##i = 1
##while i <= rows:
##    j = 1
##    while j <= i:
##        print((i*2-1),end = " ")
##        j = j +1
##    i = i +1
##    print()


# 4)

##rows = 6
##for i in range (1,rows):
##    for j in range(i,0,-1):
##        print(j,end = " ")
##    print()


# 5)

##start = 1
##stop = 2
##
##n = stop
##for row in range(2,6):
##    for col in range(start,stop):
##        n = n-1
##        print(n,end = " ")
##    print()
##    start= stop
##    stop = stop + row
##    n = stop
##
##


# 6)

##for i in range(1,8):
##    if(i==1):
##        res = i
##    else:
##        res = res * 11
##    print(res,end = " ")
##    print()


# 7)

##rows = 5
##for i in range(1,rows+1):
##    for j in range(1,rows+1):
##        if j <=i:
##            print(i,end = " ")
##        else:
##            print(j,end = " ")
##    print()
##

# 8)

##for i in range(1,9):
##    for j in range(1,i+1):
##        print(i*j,end = " ")
##    print()

# 9)


##rows = 5
##k = 2*rows - 2
##for i in range(rows,-1,-1):
##    for j in range(k,0,-1):
##        print(end = " ")
##    k = k +1
##    for j in range(0,i+1):
##        print("*",end = " ")
##    print()


# 10)

##size = 7
##m = (2 * size)-2
##
##for i in range(0,size):
##    for j in range(0,m):
##        print(end = " ")
##    m = m-1
##    for j in range(0,i+1):
##        print("* ",end = " ")
##    print()


# 11)

##n = 6
##for i in range(n):
##    for j in range(i+1):
##        print("*",end = " ")
##    print()
##print("\n")
##n = 6
##for i in range(n):
##    for j in range(i,n):
##        print("*",end = " ")
##    print()
##


# 12)

##n = 5
##for i in range(n):
##    for j in range(i+1):
##        print("*",end = " ")
##    print()
##for i in range(n):
##    for j in range(n-i-1):
##        print("*",end = " ")
##    print()


# 13)

##n = 5
##for i in range(n):
##    for j in range(n-i-1):
##        print(" ",end = " ")
##    for k in range(i+1):
##        print("*",end = " ")
##    print()
##for i in range(n-1):
##    for j in range(i+1):
##        print(" ",end = " ")
##    for k in range(n-i-1):
##        print("*",end = " ")
##    print()


# 14)

##rows = 5
##for i in range(1,rows):
##    for j in range(1,i):
##        print("",end=" ")
##
##    k = i
##    for k in range(i,rows+1):
##        print("*",end = " ")
##
##    print()
##
##i = rows - 1
##while i >= 0:
##    j = 0
##    while j<i:
##        print('',end=" ")
##        j+=1
##    k = i
##    while k<= rows - 1:
##        print("*",end = " ")
##        k +=1
##    print('')
##    i -=1
##


# 15)

##n = 20
##print("*" *n,end = "\n")
##i = (n//2)-1
##j = 2
##while i != 0:
##    while j <= (n-2):
##        print("*"*i,end = " ")
##        print("-"*j,end = " ")
##        print("*"*i)
##        i = i-1
##        j = j+2






















































            
