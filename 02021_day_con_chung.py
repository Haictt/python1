t = int(input())
for x in range(t):
    a,b,c = [int(x) for x in input().split()]
    arr_a = [int(x) for x in input().split()]
    arr_b = [int(x) for x in input().split()]
    arr_c = [int(x) for x in input().split()]
    i,j,k=0,0,0
    check = 0
    while (i < a and j < b and k < c):
        if(arr_a[i] == arr_b[j] == arr_c[k]):
            print(arr_a[i],end=' ')
            i+=1
            j+=1
            k+=1
            check = 1
        elif arr_a[i] < arr_b[j]:
            i+=1
        elif arr_b[j] < arr_c[k]:
            j+=1
        elif arr_c[k] < arr_a[i]:
            k+=1
    if check == 0:
        print("NO")
    else:
        print()
    
