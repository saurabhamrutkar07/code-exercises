n = int(input("Enter the number of input : "))

# def generste_next_value(previous_count,row):
#     return (previous_count + row)


current_number = 1 

for i in range(1,n+1):
    for j in range(i):
        print(current_number,end=' ')
        current_number += 1
    print()




    
