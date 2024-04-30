n = 9
for i in range(n):
    for j in range(n):
        if ((i<n//2) & (j<=i))  |  ((i>n//2) & (j<n-i))  |  (i==n//2):
            print("*",end='')
        else:
            print(" ",end='')
    
    #Triangle pattern
    if (i==n//2-1) | (i==n//2+1):
        print(" *",end='')
    if i==n//2:
        print("***",end='')
    print()