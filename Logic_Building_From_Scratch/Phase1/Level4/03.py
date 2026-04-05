# Take three numbers and print the median value (neither maximum nor minimum). 

try :
    numbers = list(map(int,input("Enter the numbers separated by comma , : ").split(",")) )
    numbers.sort() 
    lenght = len(numbers)
    if lenght % 2 == 0 :
        print(f"The median is {(numbers[lenght//2] + numbers[(lenght//2)- 1])/2}")
    else:
        print(f"Median is {numbers[lenght//2]}")




except Exception as e:
    print(f"Following error occurs : {e}")