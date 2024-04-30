n = 6
x = 0
for i in range(n*2):
    flag = False
    #part 1
    if i<(n+1):
        print("@",end='')
    else:
        print(" ",end='')
    #part 2
    for j in range(n*(n-1)+1):
        if (i>=n//2) & (i<(2*n)-(n//2)):
            #part 3
            if (j<(n-1)*x) | (j>(n-1)*x+n-1):
                print(" ",end='')
            else:
                print("*",end='')
                flag = True
        else:
            print(" ",end='')
    if flag:
        x = x+1
    #part4
    if i>(n-1):
        print("@",end='')
    else:
        print(" ",end='')
    print()
