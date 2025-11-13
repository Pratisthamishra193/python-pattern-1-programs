n = int(input("Enter number of rows: "))
for i in range(1, n + 1): 
    num = 1                   
    for j in range(1, i + 1):  
        if j % 2 == 1:         
            print(num, end=" ")
            num += 2
        else:                 
            print("*", end=" ")
    print()
